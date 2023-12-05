from ..utils.day import Day
from ..utils.io import read_file


class Seed:
    id: int
    _soil: int
    _fertilizer: int
    _water: int
    _light: int
    _temperture: int
    _humidity: int
    _location: int

    def __init__(self, id: int):
        self.id = id


class Day05(Day):
    def __init__(self, input_filename: str = "day05.txt") -> None:
        self.parse_data(read_file(input_filename))

    def part1(self) -> str:
        return ""

    def part2(self) -> str:
        return ""
