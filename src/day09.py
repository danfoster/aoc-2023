import os
from pprint import pprint
from typing import List


class Report:
    data: List[List[int]]

    def __init__(self, line: str):
        self.data = [[int(x) for x in line.split()]]

    @staticmethod
    def calc_diff(input: List[int]) -> List[int]:
        output: List[int] = []
        for i in range(len(input) - 1):
            output.append(input[i + 1] - input[i])
        return output

    @staticmethod
    def is_all_zeros(input: List[int]) -> bool:
        for i in input:
            if i != 0:
                return False
        return True

    def calc_diffs(self) -> None:
        data = self.data[0]
        while True:
            data = self.calc_diff(data)
            if self.is_all_zeros(data):
                break
            self.data.append(data)

    def predict_end(self) -> int:
        prev: int = 0
        for i in reversed(self.data):
            prev += i[-1]
            i.append(prev)

        return prev

    def predict_front(self) -> int:
        prev: int = 0
        for i in reversed(self.data):
            prev = i[0] - prev
            i.insert(0, prev)

        return prev


class Day09:
    def __init__(self, input_filename: str = "day09.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data = []
        lines = data.rstrip().split("\n")
        for line in lines:
            self.data.append(Report(line))

    def part1(self) -> int:
        ans: int = 0
        for report in self.data:
            report.calc_diffs()
            ans += report.predict_end()
        return ans

    def part2(self) -> int:
        ans: int = 0
        for report in self.data:
            ans += report.predict_front()
        return ans


if __name__ == "__main__":
    day = Day09()
    print(day.part1())
    print(day.part2())
