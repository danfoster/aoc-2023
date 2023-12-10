import os
from typing import Dict, List

# north = 0
# east = 1
# south = 2
# west = 3
VECTORS: Dict[int, List[int]] = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}

GREEN = "\033[32m"
RESET = "\033[0m"


class Pipe:
    inloop: bool
    d1: int
    d2: int
    start: bool

    def __init__(self, c: str | None = None, d1: int | None = 0, d2: int | None = 0):
        if c:
            self.char_to_shape(c)
        else:
            assert d1 is not None
            assert d2 is not None
            self.d1 = d1
            self.d2 = d2
        self.inloop = False
        self.start = False

    def char_to_shape(self, c: str) -> None:
        mapping = {
            "|": [0, 2],
            "-": [1, 3],
            "L": [0, 1],
            "J": [0, 3],
            "7": [2, 3],
            "F": [1, 2],
        }
        self.d1, self.d2 = mapping[c]

    def __repr__(self) -> str:
        mapping = {2: "│", 7: "─", 1: "└", 3: "┘", 11: "┐", 6: "┌"}
        return f"{mapping[(self.d1 << 2) + self.d2]}"

    @staticmethod
    def flip_dir(d: int) -> int:
        return (d + 2) % 4

    def is_joining(self, source_dir: int) -> bool:
        flipped_dir = self.flip_dir(source_dir)
        return flipped_dir == self.d1 or flipped_dir == self.d2

    def follow_pipe(self, input_dir: int) -> int:
        if self.flip_dir(input_dir) == self.d2:
            return self.d1
        return self.d2

    def shape(self) -> int:
        return (self.d1 << 2) + (self.d2 & 0x3)


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
                    row.append(Pipe(c=c))
            self.data.append(row)
        self.infer_starting_pipe()

    def print_pipes(self) -> None:
        for row in self.data:
            for pipe in row:
                if pipe:
                    if pipe.inloop:
                        print(f"{GREEN}{pipe}{RESET}", end="")
                    else:
                        print(pipe, end="")
                else:
                    print(" ", end="")
            print("")

    def get_pipe(self, x: int, y: int) -> Pipe:
        pipe = self.data[y][x]
        assert pipe is not None
        return pipe

    def infer_starting_pipe(self) -> None:
        dirs: List[int] = []
        for d, coord in VECTORS.items():
            x = self.start_x + coord[0]
            y = self.start_y + coord[1]
            pipe = self.data[y][x]
            if pipe and pipe.is_joining(d):
                dirs.append(d)

        pipe = Pipe(d1=dirs[0], d2=dirs[1])
        pipe.start = True
        self.data[self.start_y][self.start_x] = pipe

    def part1(self) -> int:
        ans: int = 1
        x = self.start_x
        y = self.start_y
        d = self.get_pipe(x, y).d1
        pipe = self.get_pipe(x, y)
        pipe.inloop = True
        while True:
            d = pipe.follow_pipe(d)
            dx, dy = VECTORS[d]
            x += dx
            y += dy
            ans += 1
            pipe = self.get_pipe(x, y)
            pipe.inloop = True
            if pipe.start:
                break

        return int(ans / 2)

    def part2(self) -> int:
        ans: int = 0
        entrance_shape: int = 0
        # self.print_pipes()
        for row in self.data:
            inside = False
            for pipe in row:
                if pipe and pipe.inloop:
                    shape = pipe.shape()
                    if shape == 2:
                        inside = not inside
                    elif shape == 7:
                        continue
                    elif entrance_shape == 0:
                        entrance_shape = shape
                    else:
                        if (
                            (entrance_shape == 1 and shape == 11)
                            or (entrance_shape == 11 and shape == 1)
                            or (entrance_shape == 6 and shape == 3)
                            or (entrance_shape == 3 and shape == 6)
                        ):
                            inside = not inside
                        entrance_shape = 0
                else:
                    entrance_shape = 0
                    if inside:
                        ans += 1

        return ans


if __name__ == "__main__":
    day = Day10()
    print(day.part1())
    print(day.part2())
