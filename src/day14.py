import copy
import os
from typing import List


class Day14:
    grid: List[List[int]]
    origgrid: List[List[int]]

    def __init__(self, input_filename: str = "day14.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.grid = []
        for line in data.rstrip().split("\n"):
            self.grid.append([ord(x) for x in line])
        self.origgrid = copy.deepcopy(self.grid)

    def reset(self) -> None:
        self.grid = copy.deepcopy(self.origgrid)

    def rotate_cw(self) -> None:
        self.grid = [list(reversed(x)) for x in zip(*self.grid)]

    def roll_row_right(self, idx: int) -> None:
        gaps = 0
        rocks = 0
        newline: List[int] = []
        for c in self.grid[idx]:
            if c == 46:  # '.'
                gaps += 1
            elif c == 79:  # 'O'
                rocks += 1
            else:  # '#'
                newline += [46] * gaps
                newline += [79] * rocks
                gaps = 0
                rocks = 0
                newline.append(35)
        newline += [46] * gaps
        newline += [79] * rocks
        self.grid[idx] = newline

    def roll_right(self) -> None:
        for i in range(len(self.grid)):
            self.roll_row_right(i)

    def score_east(self) -> int:
        ans: int = 0
        for line in self.grid:
            for i, c in enumerate(line):
                if c == 79:
                    ans += i + 1
        return ans

    def score_north(self) -> int:
        ans: int = 0
        l = len(self.grid)
        for i, line in enumerate(self.grid):
            for c in line:
                if c == 79:
                    ans += l - i
        return ans

    def grid_id(self) -> List[int]:
        _id: List[int] = []
        for line in self.grid:
            ans: int = 0
            for i, c in enumerate(line):
                if c == 79:
                    ans += i
            _id.append(ans)

        return _id

    def spin(self) -> None:
        for i in range(4):
            self.rotate_cw()
            self.roll_right()

    def print_grid(self) -> None:
        for line in self.grid:
            print("".join([chr(c) for c in line]))

    def part1(self) -> int:
        self.rotate_cw()
        self.roll_right()
        return self.score_east()

    def part2(self) -> int:
        seen_ids: List[List[int]] = []
        count = 0
        while True:
            self.spin()
            _id = self.grid_id()
            if _id in seen_ids:
                break
            seen_ids.append(_id)
            count += 1

        start_idx = seen_ids.index(_id)
        diff = count - start_idx
        after = ((1000000000 - start_idx) % diff) - 1
        for _ in range(after):
            self.spin()
        return self.score_north()


if __name__ == "__main__":
    day = Day14()
    print(day.part1())
    day.reset()
    print(day.part2())
#
