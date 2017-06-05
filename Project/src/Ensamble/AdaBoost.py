from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import f1_score
import random

from Project.src.Shared.DataReader import DataReader as dr


class ADAB:

    def __init__(self, features, classificationFeature, classes, trainigSetPath, testSetPath, delimiter, take_percentage=100, rand_seed=1):
        self.classificationFeature = classificationFeature
        reader1 = dr(features, classificationFeature, classes)
        result1 = reader1.readSet(trainigSetPath, delimiter)
        self.trainSet = self.sampling(result1["set"], take_percentage, rand_seed)
        self.trainSetClasses = self.sampling(result1["classes"], take_percentage, rand_seed)

        reader2 = dr(features, classificationFeature, classes)
        result2 = reader2.readSet(testSetPath, delimiter)
        self.testSet = self.sampling(result2["set"], take_percentage, rand_seed)
        self.testSettClasses = self.sampling(result2["classes"], take_percentage, rand_seed)
        self.clf = None

    def sampling(self, dset,  percentage, seed):
        random.seed(seed)
        k = (len(dset)*percentage)/100
        return random.sample(list(dset), int(k))

    def run(self, n_estimators = 100):
        self.clf = AdaBoostClassifier(n_estimators=n_estimators)
        self.clf.fit(self.trainSet, self.trainSetClasses)
        score = self.clf.score(self.testSet, self.testSettClasses)
        predicted = self.clf.predict(self.testSet)
        f1Score = f1_score(self.testSettClasses, predicted, average='binary', pos_label='1')

        return {
            "score": score,
            "f1_score": f1Score
        }

    def predict(self):
        clf = AdaBoostClassifier(n_estimators=100)

        clf.fit(self.trainSet, self.trainSetClasses)
        predicted = clf.predict(self.testSet)

        return {
                "prediction": predicted,
                "set": self.testSet
            }