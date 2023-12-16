import os
from collections import OrderedDict, defaultdict
from functools import cache
from pprint import pprint
from typing import DefaultDict


class HASH:
    input: str
    op: bool  # False: -,True: =
    label: str
    focal: int

    def __init__(self, input: str):
        self.input = input
        self.parse()

    def parse(self) -> None:
        if "-" in self.input:
            self.label = self.input.split("-")[0]
            self.focal = 0
            self.op = False
        elif "=" in self.input:
            self.label, focal = self.input.split("=")
            self.focal = int(focal)
            self.op = True
        else:
            assert 1, "Impossible"

    def p1(self) -> int:
        return self._hash(self.input)

    @staticmethod
    @cache
    def _hash(input: str) -> int:
        value: int = 0
        for c in input:
            value += ord(c)
            value *= 17
            value = value % 256
        return value

    @cache
    def box(self) -> int:
        return self._hash(self.label)

    def __repr__(self) -> str:
        return f"{self.label} {self.focal}"


class Day15:
    boxes: DefaultDict[int, OrderedDict[str, HASH]]

    def __init__(self, input_filename: str = "day15.txt") -> None:
        self.boxes = defaultdict(lambda: OrderedDict())
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data = [HASH(x) for x in data.rstrip().split(",")]

    def part1(self) -> int:
        return sum([x.p1() for x in self.data])

    def part2(self) -> int:
        ans: int = 0
        for lens in self.data:
            if lens.op:
                self.boxes[lens.box()][lens.label] = lens
            else:
                self.boxes[lens.box()].pop(lens.label, None)

        for box_idx, box in self.boxes.items():
            for lens_idx, lens in enumerate(box.values()):
                ans += (box_idx + 1) * (lens_idx + 1) * lens.focal
        return ans


if __name__ == "__main__":
    day = Day15()
    print(day.part1())
    print(day.part2())
