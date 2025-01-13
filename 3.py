import json
from typing import List


class BillingService:
    def __init__(self):
        self._db_file = "./assets/json_data.json"
        self.db: List

    def __init_db(self):
        with open(self._db_file, "r", encoding="utf-8") as _db:
            self.db = json.load(_db)

    def calculate_media(self):
        self.__init_db()
        media = 0
        util_days = 0
        for day in self.db:
            for k, v in day.items():
                if v > 0:
                    media += v
                    util_days += 1

        return media / util_days

    def calculate_days_with_billing_higher_than_media(self):
        media = self.calculate_media()
        days_higher_than_media = []
        for day in self.db:
            for k, v in day.items():
                if v > media:
                    days_higher_than_media.append(day)
        return days_higher_than_media

    def lowest_billing_day(self):
        self.__init_db()

        values = [(day["dia"], day["valor"]) for day in self.db if day["valor"] > 0]
        if values:
            day, value = min(values, key=lambda x: x[1])
            return {"day": day, "value": value}
        return None

    def highest_billing_day(self):
        self.__init_db()
        valores = [(day["dia"], day["valor"]) for day in self.db]
        if valores:
            day, value = max(valores, key=lambda x: x[1])
            return {"day": day, "value": value}
        return None


if __name__ == "__main__":
    bs = BillingService()
    print(bs.calculate_media(), sep="\n")
    print(bs.calculate_days_with_billing_higher_than_media(), sep="\n")
    print(bs.lowest_billing_day(), sep="\n")
    print(bs.highest_billing_day())
