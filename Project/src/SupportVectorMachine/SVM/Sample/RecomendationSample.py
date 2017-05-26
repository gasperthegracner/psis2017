from Project.src.SupportVectorMachine.SVM.SupportVectorMachine import SVM, np
from Project.src.Shared.Recomender import Recommender
from Project.helpers.RecommentationOutputBuilder import RecommendationOutputBulder as ROB

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


r = Recommender(filename="../../../../Data/clusteredIntensity_cleaned.csv",
                savetofile="../../../../Data/generated_trainings.csv")
testPath = r.generate_possible_combinations(min_intensity=0, max_intensity=1)

svm = SVM(classFeatures, classificationResult, classes, trainPath, testPath, ";")
result = svm.predict(kernel="linear")

rob = ROB(result)
json_string = rob.get_json_string(5)

print(json_string)
