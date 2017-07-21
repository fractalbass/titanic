############################################
# Titanic.py
#
# A model for predicting survival of the
# Titanic disaster.  Based on the Kaggle
# data set available at:
#
# https://www.kaggle.com/c/titanic
#
# Miles Porter
# July 19, 2017
############################################

from TitanicNetwork import TitanicNetwork

############################################
# TitanicClosestMatch.py
#
# A model for predicting survival of the
# Titanic disaster.  Based on the Kaggle
# data set available at:
#
# https://www.kaggle.com/c/titanic
#
# This model simply looks for the closest
# match for each passenger in the training
# set.
#
# Miles Porter
# July 20, 2017
############################################

from Comparator import Comparator
from FileUtils import FileUtils

class TitanicClosestMatch:

    def __init__(self):
        print("Initializing.")

    def run(self):
        futils = FileUtils(filename="./data/normalized_training_data_2.csv", skip_header=True, whitespace_delim=True)
        comp = Comparator(reference_dict=futils.get_arrays_from_csv(), start_comparison_col=2)
        predictions = []
        test_file = FileUtils(filename="./data/normalized_test_data_2.csv", skip_header=True, whitespace_delim=True)
        for test_record in test_file.get_arrays_from_csv():
            match = comp.get_closes_match(test_record)
            print("Closes match for {0} is {1}".format(test_record, match))
            predictions.append("{0},{1}".format(int(test_record[0]),int(match[1])))
        for p in predictions:
            print(p)

if __name__ == "__main__":
    titanic = TitanicClosestMatch()
    titanic.run()
