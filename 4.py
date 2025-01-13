class ExerciceFour:
    def __init__(self) -> None:
        self.data = [
            {"state": "SP", "value": 67_836.43},
            {"state": "RJ", "value": 36_678.66},
            {"state": "MG", "value": 29_229.88},
            {"state": "ES", "value": 27_165.48},
            {"state": "others", "value": 19_849.53},
        ]

        self.total = sum([d["value"] for d in self.data])

    def calculate_percent_by_state(self):
        for d in self.data:
            d["percent"] = d["value"] / self.total * 100
        return self.data


if __name__ == "__main__":
    e4 = ExerciceFour()
    res = e4.calculate_percent_by_state()
    for _ in res:
        print(_, sep="\n")
