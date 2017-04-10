from sklearn import tree

from src.Shared.DataReader import DataReader as dr


class DT:

    def __init__(self, features, classificationFeature, classes, trainigSetPath, testSetPath, delimiter):

        reader1 = dr(features, classificationFeature, classes)
        result1 = reader1.readSet(trainigSetPath, delimiter)
        self.trainSet = result1["set"]
        self.trainSetClasses = result1["classes"]

        reader2 = dr(features, classificationFeature, classes)
        result2 = reader2.readSet(testSetPath, delimiter)
        self.testSet = result2["set"]
        self.testSettClasses = result2["classes"]

    def run(self):
        clf = tree.DecisionTreeClassifier()
        clf.fit(self.trainSet, self.trainSetClasses)
        score = clf.score(self.testSet, self.testSettClasses)

        return {
            "score": score
        }

