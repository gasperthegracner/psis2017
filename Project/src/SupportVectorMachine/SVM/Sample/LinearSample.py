from Project.src.SupportVectorMachine.SVM.SupportVectorMachine import SVM, np

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

svm = SVM(classFeatures, classificationResult, classes, trainPath, testPath, ";")

result = svm.run(kernel="linear")
print("(kernel=\"linear\") Mean sample accuracy: " + str(result["score"] * 100) + "%")

# ConvergenceWarning: Solver terminated early (max_iter=50000).
# Consider pre-processing your data with StandardScaler or MinMaxScaler.% self.max_iter, ConvergenceWarning)
result = svm.run(kernel="linear", max_iter=50000)
print("(kernel=\"linear\", max_iter=50000) Mean sample accuracy: " + str(result["score"] * 100) + "%")

result = svm.run(kernel="linear", decision_function_shape="ovo")
print("(kernel=\"linear\", decision_function_shape=\"ovo\") Mean sample accuracy: " + str(result["score"] * 100) + "%")

result = svm.run(kernel="linear", decision_function_shape="ovr")
print("(kernel=\"linear\", decision_function_shape=\"ovr\") Mean sample accuracy: " + str(result["score"] * 100) + "%")

result = svm.run(kernel="linear", shrinking=False)
print("(kernel=\"linear\", shrinking=False) Mean sample accuracy: " + str(result["score"] * 100) + "%")

