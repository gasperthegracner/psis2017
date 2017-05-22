import numpy
import random
import os


class Recommender:
    '''
    Class for generating recommendation data based input parameters like min intensity,
     max intensity, min duration, max duration, min heath rate, max heath rate and training days
    '''
    def __init__(self, filename="../../Data/clusteredIntensity_cleaned.csv", savetofile="../../Data/generated_trainings.csv"):
        raw_data = numpy.genfromtxt(open(filename, 'rb'), delimiter=";", dtype=None).astype(str)
        self.data = []
        self.save_to_file = savetofile
        for ind, row in enumerate(raw_data):
            if ind == 0:
                continue

            tmpobj = {
                "avgHR": float(row[0]),
                "intensity": float(row[1]),
                "duration": float(row[3]),
                "all": [float(row[0]), float(row[1]), float(row[3])]
            }

            self.data.append(tmpobj)

    def __save_generated_trainings(self, generated):
        header_string = 'mon_intensity;mon_duration;mon_hr;tue_intensity;tue_duration;tue_hr;' \
                        'wed_intensity;wed_duration;wed_hr;thu_intensity;thu_duration;thu_hr;fri_intensity;' \
                        'fri_duration;fri_hr;sat_intensity;sat_duration;sat_hr;sun_intensity;sun_duration;sun_hr'

        path = self.save_to_file
        with open(path, 'w') as the_file:
            the_file.write(header_string+"\n")
            for g in generated:
                s = ";".join(str(g_item) for g_item in g)
                the_file.write(s + "\n")

        return os.path.abspath(path)



    def generate_possible_combinations(self, min_intensity=0, max_intensity=3, min_duration=0, max_duration=1000000, min_HR=0, max_HR=1000, days=7):
        fitted = []

        min_intensity = float(min_intensity)
        max_intensity = float(max_intensity)
        min_duration = float(min_duration)
        min_HR = float(min_HR)
        max_HR = float(max_HR)

        for row in self.data:
            if row["intensity"] > min_intensity and row["intensity"] <= max_intensity:
                if row["avgHR"] > min_HR and row["avgHR"] <= max_HR:
                    if row["duration"] > min_duration and row["duration"] <= max_duration:
                        fitted.append(row)

        # mon_intensity;mon_duration;mon_hr;tue_intensity;tue_duration;tue_hr;wed_intensity;
        # wed_duration;wed_hr;thu_intensity;thu_duration;thu_hr;fri_intensity;fri_duration;fri_hr;
        # sat_intensity;sat_duration;sat_hr;sun_intensity;sun_duration;sun_hr
        len_of_fitted = len(fitted)
        num_of_posibilities = 100
        weeks_posibilities = []
        for p in range(0, num_of_posibilities):
            num_of_true = 0
            week = []
            for i in range(0, 7):
                take_day = random.randrange(2)
                if take_day == 1 and num_of_true <= days:
                    num_of_true += 1
                    fited_ind = random.randrange(len_of_fitted)
                    week.append(fitted[fited_ind]["intensity"])
                    week.append(fitted[fited_ind]["duration"])
                    week.append(fitted[fited_ind]["avgHR"])
                else:
                    week.append(0)
                    week.append(0)
                    week.append(0)

            weeks_posibilities.append(week)
        file_path = self.__save_generated_trainings(weeks_posibilities)
        return file_path
