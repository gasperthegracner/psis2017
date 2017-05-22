from sklearn.ensemble import AdaBoostClassifier

from Project.src.Shared.DataReader import DataReader as dr


class ADAB:

    def __init__(self, features, classificationFeature, classes, trainigSetPath, testSetPath, delimiter):

        reader1 = dr(features, classificationFeature, classes)
        result1 = reader1.readSet(trainigSetPath, delimiter)
        self.trainSet = result1["set"]
        self.trainSetClasses = result1["classes"]

        reader2 = dr(features, classificationFeature, classes)
        result2 = reader2.readSet(testSetPath, delimiter)
        self.testSet = result2["set"]
        self.testSettClasses = result2["classes"]
        self.clf = None

    def run(self):
        self.clf = AdaBoostClassifier(n_estimators=100)
        self.clf.fit(self.trainSet, self.trainSetClasses)
        score = self.clf.score(self.testSet, self.testSettClasses)

        return {
            "score": score
        }

    def predict(self):
        clf = AdaBoostClassifier(n_estimators=100)

        clf.fit(self.trainSet, self.trainSetClasses)
        predicted = clf.predict(self.testSet)

        return {
                "prediction": predicted,
                "set": self.testSet
            }