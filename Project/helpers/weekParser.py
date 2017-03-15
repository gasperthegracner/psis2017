import pandas as pd
import numpy as np


class RidersWeek:
    def __init__(self, rider, weekOfYear):
        self.rider = rider
        self.WeekOfYear = weekOfYear
        self.day = {
            "Monday": {
                "intensity": 0,
                "duration": 0,
                "hr": 0
            },
            "Tuesday": {
                "intensity": 0,
                "duration": 0,
                "hr": 0
            },
            "Wednesday": {
                "intensity": 0,
                "duration": 0,
                "hr": 0
            },
            "Thursday": {
                "intensity": 0,
                "duration": 0,
                "hr": 0
            },
            "Friday": {
                "intensity": 0,
                "duration": 0,
                "hr": 0
            },
            "Saturday": {
                "intensity": 0,
                "duration": 0,
                "hr": 0
            },
            "Sunday": {
                "intensity": 0,
                "duration": 0,
                "hr": 0
            }
        }

    def setValues(self, day, intensity, duration, hr):
        self.day[day]["intensity"] = intensity
        self.day[day]["duration"] = duration
        self.day[day]["hr"] = hr

    def getAsCSV(self, delimiter):
        result = [
            "\""+self.rider+"\"",
            "\""+self.WeekOfYear+"\"",
            self.day["Monday"]["intensity"],
            self.day["Monday"]["duration"],
            self.day["Monday"]["hr"],
            self.day["Tuesday"]["intensity"],
            self.day["Tuesday"]["duration"],
            self.day["Tuesday"]["hr"],
            self.day["Wednesday"]["intensity"],
            self.day["Wednesday"]["duration"],
            self.day["Wednesday"]["hr"],
            self.day["Thursday"]["intensity"],
            self.day["Thursday"]["duration"],
            self.day["Thursday"]["hr"],
            self.day["Friday"]["intensity"],
            self.day["Friday"]["duration"],
            self.day["Friday"]["hr"],
            self.day["Saturday"]["intensity"],
            self.day["Saturday"]["duration"],
            self.day["Saturday"]["hr"],
            self.day["Sunday"]["intensity"],
            self.day["Sunday"]["duration"],
            self.day["Sunday"]["hr"]
        ]
        return (''+delimiter).join(str(x) for x in result)

class WeekParser:
    def __init__(self, path):
        self.csv_file = pd.read_csv(path, delimiter=";")

        self.riderId_index = np.where(self.csv_file.keys() == "Rider_id")[0][0]
        self.intensity_index = np.where(self.csv_file.keys() == "intensity")[0][0]
        self.hr_index = np.where(self.csv_file.keys() == "avgHeartRate")[0][0]
        self.duration_index = np.where(self.csv_file.keys() == "duration")[0][0]
        self.dateOfTraining_index = np.where(self.csv_file.keys() == "dateOfTraining")[0][0]

        self.weeks = {}
        self.weeksInd = []
        # print self.csv_file

    def getWeeks(self):
        result = []
        for line in self.csv_file.values:
            dt = pd.to_datetime(line[self.dateOfTraining_index])
            weekOfYear = str(dt.weekofyear) + "/" + str(dt.year)

            if weekOfYear not in self.weeks:
                self.weeks[weekOfYear] = {}
                self.weeks[weekOfYear]["Riders"] = []
                self.weeksInd.append(weekOfYear)

            if line[2] not in self.weeks[weekOfYear]:
                self.weeks[weekOfYear]["Riders"].append(line[self.riderId_index])
                self.weeks[weekOfYear][line[self.riderId_index]] = []

            self.weeks[weekOfYear][line[2]].append(line)

        for ind in self.weeksInd:
            for rider in self.weeks[ind]["Riders"]:
                # print "------ Rider " + rider + " -----"
                rw = RidersWeek(rider, ind)
                for training in self.weeks[ind][rider]:
                    # training = np.append(training, ind)
                    weekday = pd.to_datetime(training[self.dateOfTraining_index]).weekday_name
                    # training = np.append(training, weekday)
                    rw.setValues(weekday, training[self.intensity_index], training[self.duration_index], training[self.hr_index])
                result.append(rw)

        return result

csvHeaderResult = ["Rider", "WeekOfYear",
                   "mon_intensity", "mon_duration", "mon_hr",
                   "tue_intensity", "tue_duration", "tue_hr",
                   "wed_intensity", "wed_duration", "wed_hr",
                   "thu_intensity", "thu_duration", "thu_hr",
                   "fri_intensity", "fri_duration", "fri_hr",
                   "sat_intensity", "sat_duration", "sat_hr",
                   "sun_intensity", "sun_duration", "sun_hr",
                   ]

path = "../Data/clusteredIntensity_cleaned.csv"
outPath = "../Data/ridersWeek.csv"
wp = WeekParser(path)
results = wp.getWeeks()
delimiter = ";"
CSV_content = ""

CSV_content = (''+delimiter).join("\"" + str(x) + "\"" for x in csvHeaderResult)+"\n"
for result in results:
    CSV_content += result.getAsCSV(delimiter)+"\n"
# print CSV_content

with open(outPath, 'w') as the_file:
    the_file.write(CSV_content)
