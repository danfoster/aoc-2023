import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

VECTORS: Dict[str, List[int]] = {"U": [0, -1], "R": [1, 0], "D": [0, 1], "L": [-1, 0]}


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Instruction:
    dir: str
    length: int
    color: str
    p1: Point
    p2: Point

    def __init__(self, input: str) -> None:
        self.dir, l, c = input.split(maxsplit=2)
        self.length = int(l)
        self.color = c[2:8]

    def plot(self, x: int, y: int) -> Tuple[int, int]:
        self.p1 = Point(x, y)
        dx, dy = VECTORS[self.dir]
        x += dx * self.length
        y += dy * self.length
        self.p2 = Point(x, y)

        return (x, y)

    def update_from_color(self) -> None:
        mapping = {
            "0": "R",
            "1": "D",
            "2": "L",
            "3": "U",
        }
        self.dir = mapping[self.color[5]]
        self.length = int(self.color[:5], 16)

    def area(self) -> int:
        area: int = self.length
        area += self.p1.x * self.p2.y
        area -= self.p1.y * self.p2.x
        return area


class Day18:
    def __init__(self, input_filename: str = "day18.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.instructions = [Instruction(x) for x in data.rstrip().split("\n")]

    def plot(self) -> None:
        x: int = 0
        y: int = 0
        for instruction in self.instructions:
            x, y = instruction.plot(x, y)

    def area(self) -> int:
        return (sum([x.area() for x in self.instructions]) >> 1) + 1

    def part1(self) -> int:
        self.plot()
        return self.area()

    def part2(self) -> int:
        for x in self.instructions:
            x.update_from_color()
        self.plot()
        return self.area()


if __name__ == "__main__":
    day = Day18()
    print(day.part1())
    print(day.part2())
