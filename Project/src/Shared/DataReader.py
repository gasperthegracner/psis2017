from pathlib import Path
import numpy as np
from numpy import genfromtxt


class DataReader:

    def __init__(self, features, classification, classes):
        self.features = features
        self.classification = classification
        self.trainingSet = []
        self.classificationArr = []
        self.discreteClasses = classes

    def readSet(self, path, delimiter):
        my_file = Path(path)
        if not my_file.is_file():
            print("File does not exist!")
            return []

        self.trainingSet = genfromtxt(path, delimiter=delimiter, dtype=None).astype(str)
        self.ExtractData(self.trainingSet, True)

        return {
            "set": self.trainingSet,
            "classes": self.classificationArr
        }

    '''
        Extract and convert data
    '''
    def ExtractData(self, dataset, header):
        length = len(dataset)
        indexes = []

        if header:
            self.trainingSet = dataset
            header = dataset[0]
        #import pdb; pdb.set_trace()
        for entry in self.features:
            indexes.append(np.where(header == entry[0])[0][0])

        try:
            classInd = np.where(header == self.classification)[0][0]
            self.classificationArr = self.trainingSet[1:, classInd].astype(str)
        except:
            self.classificationArr = []
            print("Warning: no class attribute")

        self.trainingSet = self.trainingSet[1:, indexes]

        # Convert types of features
        tmp = np.empty([len(self.trainingSet[:, 0]), len(self.trainingSet[0])])
        for ind, f in enumerate(self.features):
            tmp[:, ind] = self.trainingSet[:, ind].astype(f[1])

        self.trainingSet = tmp


        # Discretization of class feature
        for ind, c in enumerate(self.classificationArr):
            c = c.replace("\"", "")
            self.classificationArr[ind] = self.discreteClasses[c]





