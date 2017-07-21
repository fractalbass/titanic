import unittest
from FileUtils import FileUtils


class FileUtilsTest(unittest.TestCase):

    def test_read_csv(self):
        f = FileUtils(filename="test_file.csv", skip_header=True)
        all_rows = f.get_arrays_from_csv()
        print("First Row: {0}".format(all_rows[0]))
        self.assertTrue(all_rows[0] == [1, 0.1, 0.2, 0.3])

    def test_read_whitespace_csv(self):
        f = FileUtils(filename="test_file_whitespace_delimited.csv", skip_header=True, whitespace_delim=True)
        all_rows = f.get_arrays_from_csv()
        print("First Row: {0}".format(all_rows[0]))
        self.assertTrue(all_rows[0] == [1, 0.1, 0.2, 0.3])


    if __name__ == '__main__':
        unittest.main()