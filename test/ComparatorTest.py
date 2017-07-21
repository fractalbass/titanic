import unittest
from Comparator import Comparator
from FileUtils import FileUtils


class ComparatorTest(unittest.TestCase):

    def test_compute_error(self):
        c = Comparator([[]],1)
        err = c.compute_error([1, 2, 3, 4], [1, 2, 3, 4])
        print("ERROR: {0}".format(err))
        self.assertTrue(err == 0.0)

    def test_compute_with_different_start_col(self):
        c = Comparator([[]], 2)
        err = c.compute_error([1, 2, 3, 4], [50, 60, 3, 4])
        print("ERROR: {0}".format(err))
        self.assertTrue(err == 0.0)

    def test_compute_error(self):
        c = Comparator([[]],1)
        err = c.compute_error([1, 3, 4, 5], [1, 2, 3, 4])
        print("ERROR: {0}".format(err))
        self.assertTrue(err == 3.0)

    def test_record_size_mismatch(self):
        c = Comparator("blah",1)
        self.assertRaises(Exception, c.compute_error, [1, 2, 3, 4], [1, 2, 3, 4, 5])
        self.assertRaises(Exception, c.compute_error, [1, 2, 3, 4, 5], [1, 2, 3, 4])

    def test_get_best_match(self):
        fu = FileUtils(filename="test_file.csv", skip_header=True)
        reference_rows = fu.get_arrays_from_csv()
        comp = Comparator(reference_rows,1)
        match = comp.get_closes_match([1, 10.0, 20.0, 30.0])
        self.assertTrue(match[0] == 3.0)

    def test_best_match_non_trivial(self):
        a = [[870,	1,	3,	0.134684136,	1,	1,	0.021730754,	0],
            [871,	0,	3,	0.875446884,	0,	0,	0.015411575,	0],
            [872,	1,	1,	1.582538598,	1,	1,	0.102578967,	0],
            [873,	0,	1,	1.111144122,    0,	0,	0.00975935,	0],
            [874,	0,	3,	1.582538598,	0,	0,	0.01756683,	0],
            [875,	1,	2,	0.942788952,	1,	0,	0.04684488,	1],
            [876,	1,	3,	0.50506551,	    0,	0,	0.014102261,	1],
            [877,	0,	3,	0.67342068,	    0,	0,	0.019217722,	0],
            [878,	0,	3,	0.639749646,	0,	0,	0.015411575,	0]]

        comp = Comparator(a, 2)
        a1 = comp.get_closes_match([0, 0, 1, 1.582538598, 1, 1, 0.102578967, 0])
        print("Match ID: {0}".format(int(a1[0])))
        self.assertTrue(int(a1[0]) == 872)
        a2 = comp.get_closes_match([0,	0,	3,	0.50506559,	    0,	0,	0.014102261,	1])
        print("Match ID: {0}".format(int(a2[0])))
        self.assertTrue(int(a2[0]) == 876)




if __name__ == '__main__':
    unittest.main()