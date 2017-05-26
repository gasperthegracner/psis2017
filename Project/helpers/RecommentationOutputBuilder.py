import random
import json


class RecommendationOutputBulder:
    def __init__(self, classification_results):
        self.possibilities = []
        self.data = classification_results["set"]
        self.results = classification_results["prediction"]

        self.__build()

    def __build(self):
        for ind, row in enumerate(self.data):
            if int(self.results[ind]) == 1:
                self.possibilities.append(row)

    def get_json_string(self, num):
        r = random.sample(self.possibilities, num)

        result = []

        for row in r:
            obj = {
                "mon_intensity": row[0],
                "mon_duration": row[1],
                "mon_hr": row[2],
                "tue_intensity": row[3],
                "tue_duration": row[4],
                "tue_hr": row[5],
                "wed_intensity": row[6],
                "wed_duration": row[7],
                "wed_hr": row[8],
                "thu_intensity": row[9],
                "thu_duration": row[10],
                "thu_hr": row[11],
                "fri_intensity": row[12],
                "fri_duration": row[13],
                "fri_hr": row[14],
                "sat_intensity": row[15],
                "sat_duration": row[16],
                "sat_hr": row[17],
                "sun_intensity": row[18],
                "sun_duration": row[19],
                "sun_hr": row[20]
            }
            result.append(obj)


        return json.dumps(result)
