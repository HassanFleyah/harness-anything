"""Produce an offline, human-only queue from fictional leave data."""
import csv
import io
import json
import sys
from datetime import date


FIELDS = {'id', 'employee', 'team', 'start', 'end'}


def validate_csv_quotes(content):
    """Reject stray quotes in unquoted fields; csv.reader validates the rest."""
    state = 'start'
    index = 0
    while index < len(content):
        char = content[index]
        if state == 'quoted':
            if char == '"':
                if index + 1 < len(content) and content[index + 1] == '"':
                    index += 1
                else:
                    state = 'closed'
        elif char in ',\r\n':
            state = 'start'
        elif char == '"':
            if state != 'start':
                raise ValueError('stray quote in unquoted CSV field')
            state = 'quoted'
        elif state == 'start':
            state = 'unquoted'
        index += 1


def parse_day(value):
    try:
        parsed = date.fromisoformat(value)
        if parsed.isoformat() != value:
            raise ValueError
        return parsed
    except ValueError as exc:
        raise ValueError('dates must be YYYY-MM-DD') from exc


def read_records(path):
    with open(path, encoding='utf-8', newline='') as handle:
        content = handle.read()
    validate_csv_quotes(content)
    with io.StringIO(content, newline='') as handle:
        reader = csv.reader(handle, strict=True)
        header = next(reader, None)
        if header is None or len(header) != len(FIELDS) or set(header) != FIELDS:
            raise ValueError(f'{path}: invalid header')
        result, seen = [], set()
        for row in reader:
            if len(row) != len(header):
                raise ValueError(f'{path}: wrong field count at line {reader.line_num}')
            record = {key: value.strip() for key, value in zip(header, row)}
            if any(not value for value in record.values()):
                raise ValueError(f'{path}: blank field at line {reader.line_num}')
            if record['id'] in seen:
                raise ValueError(f'{path}: duplicate ID {record["id"]}')
            seen.add(record['id'])
            start, end = parse_day(record['start']), parse_day(record['end'])
            if start > end:
                raise ValueError(f'{path}: start after end at line {reader.line_num}')
            result.append(record)
    return result


def build_queue(requests, schedule):
    if {r['id'] for r in requests} & {r['id'] for r in schedule}:
        raise ValueError('request and schedule IDs must not overlap')
    queue = []
    for request in sorted(requests, key=lambda item: item['id']):
        conflicts = []
        for entry in sorted(schedule, key=lambda item: item['id']):
            start, end = max(request['start'], entry['start']), min(request['end'], entry['end'])
            if request['team'] == entry['team'] and start <= end:
                conflicts.append({'id': entry['id'], 'employee': entry['employee'], 'overlap_start': start, 'overlap_end': end})
        queue.append({**request, 'status': 'PENDING_REVIEW', 'conflicts': conflicts})
    return {'requests': queue}


def main(argv):
    if len(argv) != 3:
        raise ValueError('usage: python leave_queue.py requests.csv schedule.csv')
    requests, schedule = read_records(argv[1]), read_records(argv[2])
    print(json.dumps(build_queue(requests, schedule), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main(sys.argv)
    except (OSError, UnicodeError, ValueError, csv.Error) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
