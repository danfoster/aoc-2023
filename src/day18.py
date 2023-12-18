import os
from dataclasses import dataclass
from functools import total_ordering
from typing import Dict, List, Tuple

from more_itertools import peekable

VECTORS: Dict[str, List[int]] = {"U": [0, -1], "R": [1, 0], "D": [0, 1], "L": [-1, 0]}


@dataclass
@total_ordering
class Point:
    x: int
    y: int

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x
        raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x < other.x
        raise NotImplementedError


@dataclass
@total_ordering
class Instruction:
    dir: str
    length: int
    color: str
    p1: Point
    p2: Point
    traverses: bool

    def __init__(self, input: str) -> None:
        self.dir, l, c = input.split(maxsplit=2)
        self.length = int(l)
        self.color = c[2:8]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Instruction):
            return self.p1 == other.p1
        raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Instruction):
            return self.p1 < other.p1
        raise NotImplementedError

    def plot(self, x: int, y: int, prev_dir: str, next_dir: str) -> None:
        p1 = Point(x, y)
        dx, dy = VECTORS[self.dir]
        x += dx * self.length
        y += dy * self.length
        p2 = Point(x, y)

        if self.dir in ["U", "D"]:
            self.traverses = True
            if p1.y < p2.y:
                self.p1 = p1
                self.p2 = p2
            else:
                self.p1 = p2
                self.p2 = p1
        else:
            self.traverses = prev_dir == next_dir
            if p1.x < p2.x:
                self.p1 = p1
                self.p2 = p2
            else:
                self.p1 = p2
                self.p2 = p1

    def intersects(self, y: int) -> int:
        """Reports how we intersect a instruction

        Args:
            y (int): The y position to check

        Returns:
            int: 0: Does not intersect
                 1: Intersects a vertical
                 2: Intersect a horizontal, not traversing the shape edge
                 3: Intersect a horizontal, traversing the shape edge
        """
        if self.dir in ["U", "D"]:
            if y > self.p1.y and y < self.p2.y:
                return 1
            return 0
        else:
            if y != self.p1.y:
                return 0
            elif self.traverses:
                return 3
            return 2


class Day18:
    def __init__(self, input_filename: str = "day18.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.instructions = [Instruction(x) for x in data.rstrip().split("\n")]

    def find_grid_size(self) -> Tuple[int, int, int, int]:
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0
        x = 0
        y = 0
        prev_dir: str = self.instructions[-1].dir
        instructions = peekable(self.instructions)
        for instruction in instructions:
            if instructions:
                next_dir = instructions.peek().dir
            else:
                next_dir = self.instructions[0].dir
            instruction.plot(x, y, prev_dir, next_dir)
            dx, dy = VECTORS[instruction.dir]
            prev_dir = instruction.dir
            x += dx * instruction.length
            y += dy * instruction.length
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y

        return min_x, min_y, max_x, max_y

    def count_capacity(self, min_x: int, min_y: int, max_y: int) -> int:
        totalans: int = 0
        for y in range(min_y, max_y + 1):
            inside: bool = False
            x: int = min_x
            prev_x: int = 0
            ans: int = 0
            for instruction in self.instructions:
                if instruction.p1.x < x:
                    continue
                x = instruction.p1.x
                i = instruction.intersects(y)
                if i == 1:
                    if inside:
                        ans += x - prev_x + 1
                    else:
                        ans += 1
                    prev_x = x + 1
                    inside = not inside
                elif i == 2:
                    x = instruction.p2.x
                    if inside:
                        ans += x - prev_x + 1
                    else:
                        ans += instruction.length + 1
                    prev_x = x + 1
                elif i == 3:
                    x = instruction.p2.x
                    if inside:
                        ans += x - prev_x + 1
                    else:
                        ans += instruction.length + 1
                    prev_x = x + 1
                    inside = not inside
            # print(ans)
            totalans += ans
        return totalans

    def part1(self) -> int:
        min_x, min_y, max_x, max_y = self.find_grid_size()
        self.instructions.sort()
        # self.create_grid()
        # self.dig_boundary(start_x, start_y)
        # self.print_grid()
        # print(min_x, min_y, max_x, max_y)
        return self.count_capacity(min_x, min_y, max_y)

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day18()
    print(day.part1())
    print(day.part2())
