import os
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, List, Set


@dataclass
class Point:
    _id: int
    x: int
    y: int

    def expand_universe_x(self, cols: Set[int], multiplier: int) -> None:
        count: int = 0
        for col in cols:
            if col < self.x:
                count += 1
        self.x += count * multiplier

    def expand_universe_y(self, rows: Set[int], multiplier: int) -> None:
        count: int = 0
        for row in rows:
            if row < self.y:
                count += 1
        self.y += count * multiplier

    def calc_distance(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


class Day11:
    def __init__(self, input_filename: str = "day11.txt") -> None:
        self.raw_data = self.read_file(input_filename).rstrip().split("\n")
        self.parse_data()

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self) -> None:
        self.data: List[Point] = []
        _id: int = 1
        for y, row in enumerate(self.raw_data):
            for x, c in enumerate(row):
                if c == "#":
                    self.data.append(Point(_id, x, y))
                    _id += 1
        self.width = x + 1
        self.height = y + 1

    def expand_universe(self, multiplier: int = 1) -> None:
        cols1 = set(range(self.width))
        cols2 = set([x.x for x in self.data])
        cols = cols1 - cols2
        rows1 = set(range(self.height))
        rows2 = set([x.y for x in self.data])
        rows = rows1 - rows2
        for point in self.data:
            point.expand_universe_x(cols, multiplier=multiplier)
            point.expand_universe_y(rows, multiplier=multiplier)
        pass

    def get_pairs(self) -> Iterable[tuple[Point, Point]]:
        return combinations(self.data, 2)

    def calc_ans(self, multiplier: int = 1) -> int:
        ans: int = 0
        if multiplier > 1:
            # WHY?!
            multiplier -= 1
        self.expand_universe(multiplier=multiplier)
        pairs = self.get_pairs()
        for pair in pairs:
            ans += pair[0].calc_distance(pair[1])
        return ans

    def part1(self) -> int:
        return self.calc_ans()

    def part2(self, multiplier: int = 1000000) -> int:
        return self.calc_ans(multiplier)


if __name__ == "__main__":
    day = Day11()
    print(day.part1())
    day.parse_data()
    print(day.part2())
