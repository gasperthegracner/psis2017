from Project.src.NeuralNetworks.neural_networks import NN
import numpy as np

classFeatures = [("mon_intensity", np.float),
                 ("mon_duration", np.float),
                 ("mon_hr", np.float),
                 ("tue_intensity", np.float),
                 ("tue_duration", np.float),
                 ("tue_hr", np.float),
                 ("wed_intensity", np.float),
                 ("wed_duration", np.float),
                 ("wed_hr", np.float),
                 ("thu_intensity", np.float),
                 ("thu_duration", np.float),
                 ("thu_hr", np.float),
                 ("fri_intensity", np.float),
                 ("fri_duration", np.float),
                 ("fri_hr", np.float),
                 ("sat_intensity", np.float),
                 ("sat_duration", np.float),
                 ("sat_hr", np.float),
                 ("sun_intensity", np.float),
                 ("sun_duration", np.float),
                 ("sun_hr", np.float),
                 ("weekIntensity", np.float),
                 ("weekDuration", np.float),
                 ("weekHearthrate", np.float),
                 ("weekOveral", np.float)
                 ]
classes = {
    "bad": 0,
    "good": 1
}
classificationResult = "bestAtlethes"

trainPath = "../../../Data/week_riders_random_train.csv"
testPath = "../../../Data/week_riders_random_test.csv"


nn = NN(classFeatures, classificationResult, classes, trainPath, testPath, ";")

solvers = ['lbfgs', 'sgd', 'adam']
activations = ['identity', 'logistic', 'tanh', 'relu']

itters = 100
result = {}

for iter in range(0, itters):

    for solver in solvers:
        for activation in activations:
            result.setdefault(solver + '-' + activation, {'score': 0, 'f1_score': 0})
            res_nn = nn.run(solver, activation)
            result[solver + '-' + activation]['score'] += res_nn['score']
            result[solver + '-' + activation]['f1_score'] += res_nn['f1_score']

    print("Hello " + str(iter) + "%")

result2 = {}
for key, value in result.items():
    result2[key] = value / itters

print(result)
