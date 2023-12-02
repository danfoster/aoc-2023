from ..utils.day import Day
from ..utils.io import read_file



class Day${DAY}(Day):
    def __init__(self, input_filename: str = "day${DAY}.txt") -> None:
        self.data = self.parse_data(read_file(input_filename))

    def part1(self) -> str:
        return ""

    def part2(self) -> str:
        return ""

