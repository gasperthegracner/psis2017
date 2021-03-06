from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score

from Project.src.Shared.DataReader import DataReader as dr


class NN:

    def __init__(self, features, classificationFeature, classes, trainigSetPath, testSetPath, delimiter):
        """ Main class forNeural Networks
        """
        self.classificationFeature = classificationFeature
        reader1 = dr(features, classificationFeature, classes)
        result1 = reader1.readSet(trainigSetPath, delimiter)
        self.trainSet = result1["set"]
        self.trainSetClasses = result1["classes"]

        reader2 = dr(features, classificationFeature, classes)
        result2 = reader2.readSet(testSetPath, delimiter)
        self.testSet = result2["set"]
        self.testSettClasses = result2["classes"]

    def run(self, solver="sgd", activation="tanh", hidden_size=(100, 100, 100)):
        """ Run neural networks classifier
        """
        clf = MLPClassifier(activation=activation,
                            solver=solver,
                            hidden_layer_sizes=hidden_size)
        clf.fit(self.trainSet, self.trainSetClasses)
        score = clf.score(self.testSet, self.testSettClasses)
        predicted = clf.predict(self.testSet)
        f1Score = f1_score(self.testSettClasses, predicted, average='binary', pos_label='1')

        return {
            "score": score,
            "f1_score": f1Score
        }

    def predict(self, solver="sgd", activation="tanh", hidden_size=(100, 1000)):
        clf = MLPClassifier(activation=activation,
                            solver=solver,
                            hidden_layer_sizes=hidden_size)

        clf.fit(self.trainSet, self.trainSetClasses)
        predicted = clf.predict(self.testSet)

        return {
                "prediction": predicted,
                "set": self.testSet
            }
