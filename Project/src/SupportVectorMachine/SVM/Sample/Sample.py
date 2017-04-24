from src.SupportVectorMachine.SVM.SupportVectorMachine import SVM, np

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
# result = svm.run(kernel="poly")
# result = svm.run(kernel="rbr")
# result = svm.run(kernel="sigmoid")

#Consider pre-processing your data with StandardScaler or MinMaxScaler.


print("Mean sample accuracy: " + str(result["score"] * 100) + "%")
