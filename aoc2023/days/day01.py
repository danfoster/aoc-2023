import re
from dataclasses import dataclass
from functools import total_ordering
from pprint import pprint
from typing import List

from ..utils.day import Day
from ..utils.io import read_file

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


class Day01(Day):
    def __init__(self, input_filename: str = "day01.txt") -> None:
        self.data = self.parse_data(read_file(input_filename))

    @staticmethod
    def extract_digits(line: str) -> List[NumberPos]:
        numbers: List[NumberPos] = []
        for i, c in enumerate(line):
            try:
                int(c)
                numbers.append(NumberPos(i, c))
            except ValueError:
                pass

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

    def part1(self) -> str:
        total: int = 0
        for line in self.data:
            numbers = self.extract_digits(line)
            s = self.concat_first_last(numbers)
            total += int(s)
        return str(total)

    def part2(self) -> str:
        total: int = 0
        for line in self.data:
            numbers = self.extract_digits(line)
            numbers += self.extract_words(line)
            s = self.concat_first_last(numbers)
            total += int(s)
        return str(total)


def main() -> None:
    day = Day01()
    pprint(day.part1())


if __name__ == "__main__":
    main()
