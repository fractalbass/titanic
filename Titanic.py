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


class Titanic:

    def __init__(self):
        print("Initializing.")

    def run(self):

        titanic_network = TitanicNetwork('./data/normalized_training_data.csv', './data/normalized_testing_data.csv')
        #titanic_network.train()
        #titanic_network.save_model("saved_titanic_network_4x120")
        titanic_network.load_model("saved_titanic_network_4x120")
        #titanic_network.display_training_results()
        survival = titanic_network.predict()
        print("Complete.  Survival rate: {0}".format(survival))


if __name__ == "__main__":
    titanic = Titanic()
    titanic.run()
