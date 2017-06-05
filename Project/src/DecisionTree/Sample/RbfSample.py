from Project.src.DecisionTree.DecisionTree import DT
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
                 ("sun_hr", np.float)#,
                 # ("weekIntensity", np.float),
                 # ("weekDuration", np.float),
                 # ("weekHearthrate", np.float),
                 # ("weekOveral", np.float)
                 ]
classes = {
    "bad": 0,
    "good": 1
}
classificationResult = "bestAtlethes"

trainPath = "../../../Data/week_riders_random_train.csv"
testPath = "../../../Data/week_riders_random_test.csv"

result = [{"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0}]
itters = 100

for i in range(0, itters):
    dt = DT(classFeatures, classificationResult, classes, trainPath, testPath, delimiter=";", take_percentage=70, rand_seed=i)

    r_tmp = dt.run(
        criterion='gini',
        splitter='best',
        max_depth=None,
        min_samples_split=2
    )
    result[0]["score"] += r_tmp["score"]
    result[0]["f1_score"] += r_tmp["f1_score"]

    r_tmp = dt.run(
        criterion='entropy',
        splitter='best',
        max_depth=None,
        min_samples_split=2
    )
    result[1]["score"] += r_tmp["score"]
    result[1]["f1_score"] += r_tmp["f1_score"]

    r_tmp = dt.run(
        criterion='gini',
        splitter='random',
        max_depth=None,
        min_samples_split=2
    )
    result[2]["score"] += r_tmp["score"]
    result[2]["f1_score"] += r_tmp["f1_score"]

    r_tmp = dt.run(
        criterion='entropy',
        splitter='random',
        max_depth=None,
        min_samples_split=2
    )
    result[3]["score"] += r_tmp["score"]
    result[3]["f1_score"] += r_tmp["f1_score"]

    r_tmp = dt.run(
        criterion='gini',
        splitter='best',
        max_depth=11,
        min_samples_split=2
    )
    result[4]["score"] += r_tmp["score"]
    result[4]["f1_score"] += r_tmp["f1_score"]

for item in result:
    item["score"] = item["score"] / itters
    item["f1_score"] = item["f1_score"] / itters


print("(gini, best) Mean sample accuracy: " + str(round(result[0]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[0]["f1_score"], 4)))
print("(entropy, best) Mean sample accuracy: " + str(round(result[1]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[1]["f1_score"], 4)))
print("(gini, random) Mean sample accuracy: " + str(round(result[2]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[2]["f1_score"], 4)))
print("(entropy, random) Mean sample accuracy: " + str(round(result[3]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[3]["f1_score"], 4)))
print("(gini, best, max_depth = 9, min_samples_split = 5) Mean sample accuracy: " + str(round(result[4]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[4]["f1_score"], 4)))

