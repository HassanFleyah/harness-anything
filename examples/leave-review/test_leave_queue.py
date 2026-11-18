import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parent / 'leave-review-skill' / 'scripts' / 'leave_queue.py'
HEADER = ['id', 'employee', 'team', 'start', 'end']


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.request = Path(self.directory.name) / 'requests.csv'
        self.schedule = Path(self.directory.name) / 'schedule.csv'

    def write(self, path, rows, header=HEADER):
        with path.open('w', encoding='utf-8', newline='') as target:
            writer = csv.writer(target)
            writer.writerow(header)
            writer.writerows(rows)

    def run_report(self):
        return subprocess.run([sys.executable, '-B', str(SCRIPT), str(self.request), str(self.schedule)], capture_output=True, text=True)

    def test_human_review_and_endpoint_overlap(self):
        self.write(self.request, [['R2', 'Cal', 'Birch', '2026-12-01', '2026-12-02'], ['R1', 'Alex', ' Cedar ', '2026-12-03', '2026-12-04']])
        self.write(self.schedule, [['S2', 'Alex', 'Cedar', '2026-12-03', '2026-12-03'], ['S1', 'Bea', 'Cedar', '2026-12-04', '2026-12-05'], ['S3', 'Dee', 'Birch', '2026-12-03', '2026-12-03']])
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        entries = json.loads(result.stdout)['requests']
        self.assertEqual([item['id'] for item in entries], ['R1', 'R2'])
        self.assertEqual([item['status'] for item in entries], ['PENDING_REVIEW', 'PENDING_REVIEW'])
        self.assertEqual(entries[0]['conflicts'], [{'id': 'S1', 'employee': 'Bea', 'overlap_start': '2026-12-04', 'overlap_end': '2026-12-04'}, {'id': 'S2', 'employee': 'Alex', 'overlap_start': '2026-12-03', 'overlap_end': '2026-12-03'}])
        self.assertEqual(entries[1]['conflicts'], [])

    def test_empty_and_reordered_header(self):
        self.write(self.request, [], ['team', 'id', 'employee', 'end', 'start'])
        self.write(self.schedule, [])
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {'requests': []})

    def test_invalid_rows_prevent_partial_output(self):
        invalid = [['R2', '', 'Birch', '2026-12-01', '2026-12-02'], ['R2', 'Cal', 'Birch', '20261201', '2026-12-02'], ['R2', 'Cal', 'Birch', '2026-12-03', '2026-12-02'], ['R1', 'Cal', 'Birch', '2026-12-01', '2026-12-02']]
        self.write(self.schedule, [])
        for row in invalid:
            with self.subTest(row=row):
                self.write(self.request, [['R1', 'Alex', 'Cedar', '2026-12-03', '2026-12-04'], row])
                result = self.run_report()
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, '')

    def test_bad_headers_counts_and_shared_ids_fail(self):
        self.write(self.schedule, [['R1', 'Bea', 'Cedar', '2026-12-04', '2026-12-05']])
        self.write(self.request, [['R1', 'Alex', 'Cedar', '2026-12-03', '2026-12-04']])
        result = self.run_report()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        for header in [['id', 'id', 'team', 'start', 'end'], HEADER + ['extra']]:
            self.write(self.request, [], header)
            result = self.run_report()
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, '')
        self.write(self.request, [['R2', 'Alex']])
        result = self.run_report()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')

    def test_missing_file_fails_without_partial_output(self):
        self.write(self.request, [])
        result = self.run_report()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')

    def test_unescaped_quote_rejected_valid_quoted_field_accepted(self):
        self.write(self.schedule, [])
        self.request.write_text('id,employee,team,start,end\nR1,Al"ex,Cedar,2026-12-03,2026-12-04\n', encoding='utf-8')
        result = self.run_report()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        self.write(self.request, [['R1', 'Alex "A", Jr', 'Cedar', '2026-12-03', '2026-12-04']])
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['requests'][0]['employee'], 'Alex "A", Jr')


if __name__ == '__main__':
    unittest.main()
