import os
import re
from dataclasses import dataclass
from functools import total_ordering
from typing import List

numberWords = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


@dataclass
@total_ordering
class NumberPos:
    pos: int
    value: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NumberPos):
            return NotImplemented
        return self.pos == other.pos

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, NumberPos):
            return NotImplemented
        return self.pos < other.pos


class Day01:
    def __init__(self, input_filename: str = "day01.txt") -> None:
        self.numbers: List[List[NumberPos]] = []
        self.parse_data(self.read_file(input_filename))

    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")

    @staticmethod
    def get_input_dir() -> str:
        path = os.path.abspath(__file__)
        path = f"{path}/../../../inputs/"
        return os.path.abspath(path)

    @classmethod
    def read_file(cls, filename: str) -> str:
        with open(os.path.join(cls.get_input_dir(), filename), "r") as file:
            return file.read()

    @staticmethod
    def extract_digits(line: str) -> List[NumberPos]:
        numbers: List[NumberPos] = []
        for i, c in enumerate(line):
            if c.isnumeric():
                numbers.append(NumberPos(i, c))

        return numbers

    @staticmethod
    def extract_words(line: str) -> List[NumberPos]:
        numbers: List[NumberPos] = []
        for k in numberWords.keys():
            matches = re.finditer(k, line)
            for match in matches:
                numbers.append(NumberPos(match.start(), numberWords[k]))
        return numbers

    @staticmethod
    def concat_first_last(numbers: List[NumberPos]) -> str:
        numbers.sort()
        return numbers[0].value + numbers[-1].value

    def part1(self) -> int:
        total: int = 0
        for line in self.data:
            numbers = self.extract_digits(line)
            self.numbers.append(numbers)
            try:
                s = self.concat_first_last(numbers)
                total += int(s)
            except IndexError:
                pass
        return total

    def part2(self) -> int:
        total: int = 0
        for n, line in enumerate(self.data):
            numbers = self.numbers[n]
            numbers += self.extract_words(line)
            s = self.concat_first_last(numbers)
            total += int(s)
        return total
