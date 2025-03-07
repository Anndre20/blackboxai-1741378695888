# Unit Tests for File Sorting Module

import unittest
from sorting import sort_files

class TestSorting(unittest.TestCase):
    def test_sort_files(self):
        # Assuming a test directory 'test_files' with sample files
        sorted_files, file_metadata = sort_files('test_files')
        self.assertTrue(sorted_files)  # Check if sorting returns a list
        self.assertIsInstance(sorted_files, list)  # Ensure sorted_files is a list
        self.assertEqual(len(sorted_files), len(file_metadata))  # Ensure the lengths match
        self.assertTrue(all(isinstance(file, str) for file in sorted_files))  # Ensure all sorted files are strings
        
        # Filter out files with None expiration dates
        files_with_dates = [(f, m) for f, m in zip(sorted_files, file_metadata) if m.get('expiration_date') is not None]
        if files_with_dates:
            dated_files, dated_metadata = zip(*files_with_dates)
            # Check if files with dates are sorted by expiration date
            self.assertEqual(
                list(dated_files),
                sorted(dated_files, key=lambda x: next(m['expiration_date'] for f, m in files_with_dates if f == x))
            )

if __name__ == '__main__':
    unittest.main()
