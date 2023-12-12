import os
from functools import cache


class Row:
    def __init__(self, line: str):
        self.left, right = line.split(maxsplit=1)
        self.right = [int(x) for x in right.split(",")]
        # self.left += "."
        self.l_len = len(self.left)
        self.r_len = len(self.right)

    def multiply_inputs(self, multiple: int) -> None:
        self.left = "?".join([self.left] * multiple)
        self.right *= multiple
        self.l_len = len(self.left)
        self.r_len *= multiple
        self._calc.cache_clear()

    def __repr__(self) -> str:
        return f"{self.left} {self.right}"

    def calc(self) -> int:
        return self._calc(0, 0, 0)

    @cache
    def _calc(self, l_pos: int, r_pos: int, group_size: int) -> int:
        if l_pos >= self.l_len:
            if r_pos < self.r_len and group_size == self.right[r_pos]:
                # Close the final group if needed
                r_pos += 1
                group_size = 0
            if r_pos == self.r_len and group_size == 0:
                return 1
            return 0
        solutions = 0
        c = self.left[l_pos]
        if c == "?":
            fork = ["#", "."]
        else:
            fork = [c]
        for c in fork:
            if c == "#":
                solutions += self._calc(l_pos + 1, r_pos, group_size + 1)
            elif r_pos < self.r_len and group_size == self.right[r_pos]:
                # Group is complete
                solutions += self._calc(l_pos + 1, r_pos + 1, 0)
            elif group_size == 0:
                solutions += self._calc(l_pos + 1, r_pos, 0)
        return solutions


class Day12:
    def __init__(self, input_filename: str = "day12.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data = [Row(x) for x in data.rstrip().split("\n")]

    def part1(self) -> int:
        return sum([x.calc() for x in self.data])

    def part2(self) -> int:
        for x in self.data:
            x.multiply_inputs(5)
        return sum([x.calc() for x in self.data])


if __name__ == "__main__":
    day = Day12()
    print(day.part1())
    print(day.part2())
