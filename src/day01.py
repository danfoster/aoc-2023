import os
from typing import List

numberWords = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


class Day01:
    def __init__(self, input_filename: str = "day01.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    @staticmethod
    def extract_digits(line: str) -> List[str]:
        numbers: List[str] = []
        for i, c in enumerate(line):
            if c.isnumeric():
                numbers.append(c)
        return numbers

    @staticmethod
    def replace_words(line: str) -> str:
        for k in numberWords.keys():
            line = line.replace(k, numberWords[k])
        return line

    @staticmethod
    def concat_first_last(numbers: List[str]) -> str:
        return numbers[0] + numbers[-1]

    def part1(self) -> int:
        total: int = 0
        for line in self.data:
            numbers = self.extract_digits(line)
            s = self.concat_first_last(numbers)
            total += int(s)
        return total

    def part2(self) -> int:
        total: int = 0
        for n, line in enumerate(self.data):
            line = self.replace_words(line)
            numbers = self.extract_digits(line)
            s = self.concat_first_last(numbers)
            total += int(s)
        return total


if __name__ == "__main__":
    for i in range(0, 1000):
        day = Day01()
        print(day.part1())
        print(day.part2())
