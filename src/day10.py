import os
from pprint import pprint
from typing import Dict, List

# north = 0
# east = 1
# south = 2
# west = 3

VECTORS: Dict[int, List[int]] = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}


class Pipe:
    shape: int

    def __init__(self, c: str):
        self.shape = self.char_to_shape(c)

    @staticmethod
    def char_to_shape(c: str) -> int:
        mapping = {"|": 2, "-": 7, "L": 1, "J": 3, "7": 11, "F": 9}
        return mapping[c]

    def __repr__(self) -> str:
        mapping = {2: "│", 7: "─", 1: "└", 3: "┘", 11: "┐", 9: "┌"}
        return f"{mapping[self.shape]}"

    def get_dirs(self) -> (int, int):
        d1 = self.shape & 0x3
        d2 = self.shape >> 2
        return (d1, d2)

    @staticmethod
    def flip_dir(d: int) -> int:
        return (d + 2) % 4

    def is_joining(self, source_dir: int) -> bool:
        flipped_dir = self.flip_dir(source_dir)
        return flipped_dir in self.get_dirs()

    def follow_pipe(self, input_dir: int) -> int:
        d1: int
        d2: int
        d1, d2 = self.get_dirs()
        if self.flip_dir(input_dir) == d2:
            return d1
        return d2


class Day10:
    start_x: int
    start_y: int
    data: List[List[Pipe | None]]

    def __init__(self, input_filename: str = "day10.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data: List[List[Pipe | None]] = []
        for y, line in enumerate(data.rstrip().split("\n")):
            row: List[Pipe | None] = []
            for x, c in enumerate(line):
                if c == ".":
                    row.append(None)
                elif c == "S":
                    row.append(None)
                    self.start_x = x
                    self.start_y = y
                else:
                    row.append(Pipe(c))
            self.data.append(row)

    def print_pipes(self) -> None:
        for row in self.data:
            for pipe in row:
                if pipe:
                    print(pipe, end="")
                else:
                    print(".", end="")
            print("")

    def get_pipe(self, x: int, y: int) -> Pipe:
        pipe = self.data[y][x]
        assert pipe is not None
        return pipe

    def find_starting_pipe(self) -> (int, int, int):
        for d, coord in VECTORS.items():
            x = self.start_x + coord[0]
            y = self.start_y + coord[1]
            pipe = self.data[y][x]
            if pipe:
                if pipe.is_joining(d):
                    return (x, y, d)

    def part1(self) -> int:
        ans: int = 1
        # self.print_pipes()
        x, y, d = self.find_starting_pipe()
        # print(f"START: {self.start_x} {self.start_y}")
        # print(x, y, d)
        while x != self.start_x or y != self.start_y:
            pipe = self.get_pipe(x, y)
            d = pipe.follow_pipe(d)
            dx, dy = VECTORS[d]
            x += dx
            y += dy
            ans += 1
            # print(x, y, d)

        return int(ans / 2)

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day10()
    print(day.part1())
    print(day.part2())
