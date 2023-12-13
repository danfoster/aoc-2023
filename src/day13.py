import os
from functools import cache
from typing import List


class Grid:
    grid: List[str]
    width: int
    height: int

    def __init__(self) -> None:
        self.grid = []

    def __repr__(self) -> str:
        return "\n".join(self.grid) + "\n\n"

    def process(self) -> None:
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def add_row(self, line: str) -> None:
        self.grid.append(line)

    @cache
    def get_row(self, i: int) -> int:
        ans: int = 0
        for n, c in enumerate(self.grid[i]):
            if c == "#":
                ans += 1 << (n + 1)
        return ans

    @cache
    def get_col(self, i: int) -> int:
        ans: int = 0
        for n in range(self.height):
            c = self.grid[n][i]
            if c == "#":
                ans += 1 << (n + 1)
        return ans

    @cache
    def is_reflected_row(self, index: int) -> bool:
        idx1 = index
        idx2 = index + 1
        while True:
            if idx2 >= self.height or idx1 < 0:
                return True
            if self.get_row(idx1) != self.get_row(idx2):
                return False
            idx1 -= 1
            idx2 += 1

    @cache
    def is_reflected_col(self, index: int) -> bool:
        idx1 = index
        idx2 = index + 1
        while True:
            if idx2 >= self.width or idx1 < 0:
                return True
            if self.get_col(idx1) != self.get_col(idx2):
                return False
            idx1 -= 1
            idx2 += 1

    def find_reflected_row(self) -> int:
        for y in range(self.height - 1):
            if self.is_reflected_row(y):
                return y + 1
        return 0

    def find_reflected_col(self) -> int:
        for x in range(self.width - 1):
            if self.is_reflected_col(x):
                return x + 1
        return 0

    def summarize(self) -> int:
        return (self.find_reflected_row() * 100) + self.find_reflected_col()


class Day13:
    grids: List[Grid]

    def __init__(self, input_filename: str = "day13.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.grids = []
        grid = Grid()
        for line in data.rstrip().split("\n"):
            if line == "":
                grid.process()
                self.grids.append(grid)
                grid = Grid()
            else:
                grid.add_row(line)
        grid.process()
        self.grids.append(grid)

    def part1(self) -> int:
        return sum([grid.summarize() for grid in self.grids])

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day13()
    print(day.part1())
    print(day.part2())
