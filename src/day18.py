import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

VECTORS: Dict[str, List[int]] = {"U": [0, -1], "R": [1, 0], "D": [0, 1], "L": [-1, 0]}


@dataclass
class Instruction:
    dir: str
    length: int
    color: str

    def __init__(self, input: str) -> None:
        self.dir, l, c = input.split(maxsplit=2)
        self.length = int(l)
        self.color = c[2:8]


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
        for instruction in self.instructions:
            dx, dy = VECTORS[instruction.dir]
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

        start_x = abs(min_x)
        start_y = abs(min_y)
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        return start_x, start_y, width, height

    def create_grid(self) -> None:
        self.grid = [[False] * self.width for _ in range(self.height)]

    def print_grid(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def dig_boundary(self, x: int, y: int) -> None:
        self.grid[y][x] = True
        for instruction in self.instructions:
            dx, dy = VECTORS[instruction.dir]
            for _ in range(instruction.length):
                x += dx
                y += dy
                self.grid[y][x] = True

    def shape(self, x: int, y: int) -> int:
        shape: int = 0
        if y > 0:
            shape += self.grid[y - 1][x] << 0
        if x < self.width - 1:
            shape += self.grid[y][x + 1] << 1
        if y < self.height - 1:
            shape += self.grid[y + 1][x] << 2
        if x != 0:
            shape += self.grid[y][x - 1] << 3
        return shape

    def count_capacity(self) -> int:
        ans: int = 0
        entrance_shape: int = 0
        for y, line in enumerate(self.grid):
            inside: bool = False
            for x, c in enumerate(line):
                if c:
                    ans += 1
                    shape = self.shape(x, y)
                    if shape == 5:
                        inside = not inside
                    elif shape == 10:
                        continue
                    elif entrance_shape == 0:
                        entrance_shape = shape
                    else:
                        if (
                            (entrance_shape == 6 and shape == 9)
                            or (entrance_shape == 9 and shape == 6)
                            or (entrance_shape == 3 and shape == 12)
                            or (entrance_shape == 12 and shape == 3)
                        ):
                            inside = not inside
                        entrance_shape = 0

                elif inside:
                    ans += 1
        return ans

    def part1(self) -> int:
        start_x, start_y, self.width, self.height = self.find_grid_size()
        self.create_grid()
        self.dig_boundary(start_x, start_y)
        # self.print_grid()
        return self.count_capacity()

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day18()
    print(day.part1())
    print(day.part2())
