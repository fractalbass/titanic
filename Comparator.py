
class Comparator(object):

    def __init__(self, reference_dict, start_comparison_col):
        self.reference_dict = reference_dict
        self.start_col = start_comparison_col

    def get_closes_match(self, input_array):
        winning_record = self.reference_dict[0]
        err = self.compute_error(input_array, winning_record)
        for record in self.reference_dict:
            temp_err = self.compute_error(input_array, record)
            if temp_err < err:
                err = temp_err
                winning_record = record

        return winning_record

    def compute_error(self, input_array, reference_record):
        if len(input_array)!=len(reference_record):
            raise Exception("Cannot compute error for records due to size")
        # print("Input: {0}".format(input_array))
        # print("Output: {0}".format(reference_record))
        e = 0
        for i in range(self.start_col, len(reference_record)):
            e = e + ((input_array[i] - reference_record[i]) ** 2)

        return e
