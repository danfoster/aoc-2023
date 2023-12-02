from pprint import pprint

from ..utils.day import Day
from ..utils.io import read_file


class Day02(Day):
    def __init__(self, input_filename: str = "day02.txt") -> None:
        self.data = self.parse_data(read_file(input_filename))

    def part1(self) -> str:
        pprint(self.data)
        return ""

    def part2(self) -> str:
        return ""
