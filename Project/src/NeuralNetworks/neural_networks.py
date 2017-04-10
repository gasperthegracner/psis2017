from sklearn.neural_network import MLPClassifier
import numpy as np
from src.Shared.DataReader import DataReader as dr


class NN:

    def __init__(self, features, classificationFeature, classes, trainigSetPath, testSetPath, delimiter):
        """ Main class forNeural Networks
        """
        reader1 = dr(features, classificationFeature, classes)
        result1 = reader1.readSet(trainigSetPath, delimiter)
        self.trainSet = result1["set"]
        self.trainSetClasses = result1["classes"]

        reader2 = dr(features, classificationFeature, classes)
        result2 = reader2.readSet(testSetPath, delimiter)
        self.testSet = result2["set"]
        self.testSettClasses = result2["classes"]

    def run(self):
        """ Run neural networks classifier
        """
        clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(1, 1000))
        clf.fit(self.trainSet, self.trainSetClasses)
        score = clf.score(self.testSet, self.testSettClasses)

        return {
            "score": score
        }
