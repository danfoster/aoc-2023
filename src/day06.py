import os
from dataclasses import dataclass
from math import ceil, floor, sqrt


@dataclass
class Race:
    time: int
    distance: int

    def number_way_to_win(self) -> int:
        q = sqrt(self.time * self.time - 4 * self.distance)
        start = floor((self.time - q) / 2 + 1)
        end = ceil((self.time + q) / 2 - 1)
        return end - start + 1


class Day06:
    def __init__(self, input_filename: str = "day06.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        lines = data.rstrip().split("\n")
        times = lines[0].split(":", maxsplit=1)[1].split()
        distances = lines[1].split(":", maxsplit=1)[1].split()
        self.data_p1 = [Race(int(x[0]), int(x[1])) for x in zip(times, distances)]
        self.data_p2 = Race(int("".join(times)), int("".join(distances)))

    def part1(self) -> int:
        ans: int = 1
        for race in self.data_p1:
            ans *= race.number_way_to_win()
        return ans

    def part2(self) -> int:
        return self.data_p2.number_way_to_win()
