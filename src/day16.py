import os
from copy import deepcopy
from functools import cached_property
from typing import Dict, List

# north = 0
# east = 1
# south = 2
# west = 3
VECTORS: Dict[int, List[int]] = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}


class Beam:
    x: int
    x: int
    dir: int

    def __init__(self, x: int, y: int, dir: int, control: "Day16"):
        self.x = x
        self.y = y
        self.dir = dir
        self.control = control

    def _move(self) -> None:
        dx, dy = VECTORS[self.dir]
        self.x += dx
        self.y += dy

    def shoot(self) -> None:
        while True:
            e = self.control.energized[self.y][self.x]
            if self.dir in e:
                break
            e.append(self.dir)
            c = self.control.data[self.y][self.x]
            if c == "-" and self.dir in [0, 2]:
                beam = Beam(self.x, self.y, 3, self.control)
                beam.shoot()
                self.dir = 1
            if c == "|" and self.dir in [1, 3]:
                beam = Beam(self.x, self.y, 2, self.control)
                beam.shoot()
                self.dir = 0
            elif c == "\\":
                map = {
                    1: 2,
                    0: 3,
                    2: 1,
                    3: 0,
                }
                self.dir = map[self.dir]
            elif c == "/":
                map = {
                    1: 0,
                    0: 1,
                    2: 3,
                    3: 2,
                }
                self.dir = map[self.dir]

            self._move()
            if (
                self.x < 0
                or self.x >= self.control.map_width
                or self.y < 0
                or self.y >= self.control.map_height
            ):
                break

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"


class Day16:
    data: List[str]
    energized: List[List[List[int]]]

    def __init__(self, input_filename: str = "day16.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @cached_property
    def map_width(self) -> int:
        return len(self.data[0])

    @cached_property
    def map_height(self) -> int:
        return len(self.data)

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")
        self.energized = [
            [[] for i in range(len(self.data[0]))] for i in range(len(self.data))
        ]

    def print_map(self) -> None:
        for line in self.data:
            print(line)

    def print_energized(self) -> None:
        for line in self.energized:
            print("".join(["#" if len(x) > 0 else "." for x in line]))

    def count_energized(self) -> int:
        ans: int = 0
        for line in self.energized:
            ans += sum([1 if len(x) > 0 else 0 for x in line])
        return ans

    def part1(self) -> int:
        beam = Beam(0, 0, 1, self)
        self.print_map()
        beam.shoot()

        print()
        self.print_energized()
        return self.count_energized()

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day16()
    print(day.part1())
    print(day.part2())
