from Project.src.SupportVectorMachine.SVM.SupportVectorMachine import SVM
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

trainPath = "../../../../Data/week_riders_random_train.csv"
testPath = "../../../../Data/week_riders_random_test.csv"


result = [{"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0},
          {"score": 0, "f1_score": 0}]
itters = 100

for i in range(0, itters):
    svm = SVM(classFeatures, classificationResult, classes, trainPath, testPath, ";", take_percentage=70, rand_seed=i)

    r_tmp = svm.run(kernel="linear")
    result[0]["score"] += r_tmp["score"]
    result[0]["f1_score"] += r_tmp["f1_score"]

    r_tmp = svm.run(kernel="linear", max_iter=50000)
    result[1]["score"] += r_tmp["score"]
    result[1]["f1_score"] += r_tmp["f1_score"]

    r_tmp = svm.run(kernel="linear", decision_function_shape="ovo")
    result[2]["score"] += r_tmp["score"]
    result[2]["f1_score"] += r_tmp["f1_score"]

    r_tmp = svm.run(kernel="linear", decision_function_shape="ovr")
    result[3]["score"] += r_tmp["score"]
    result[3]["f1_score"] += r_tmp["f1_score"]

    r_tmp = svm.run(kernel="linear", shrinking=False)
    result[4]["score"] += r_tmp["score"]
    result[4]["f1_score"] += r_tmp["f1_score"]

for item in result:
    item["score"] = item["score"] / itters
    item["f1_score"] = item["f1_score"] / itters


print("(kernel=\"linear\") Mean sample accuracy: " + str(round(result[0]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[0]["f1_score"], 4)))
print("(kernel=\"linear\", max_iter=50000) Mean sample accuracy: " + str(round(result[1]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[1]["f1_score"], 4)))
print("(kernel=\"linear\", decision_function_shape=\"ovo\") Mean sample accuracy: " + str(round(result[2]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[2]["f1_score"], 4)))
print("(kernel=\"linear\", decision_function_shape=\"ovr\") Mean sample accuracy: " + str(round(result[3]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[3]["f1_score"], 4)))
print("(kernel=\"linear\", shrinking=False) Mean sample accuracy: " + str(round(result[4]["score"] * 100, 2)) + "%; F1 score: " + str(round(result[4]["f1_score"], 4)))
