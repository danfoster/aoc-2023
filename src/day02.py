import os
from typing import Dict


class Game:
    def __init__(self, line: str):
        parts = line.split(": ", maxsplit=1)
        self.id = int(parts[0].split(maxsplit=1)[1])
        self.max_seen: Dict[str, int] = {}

        for part in parts[1].split("; "):
            for color in part.split(", "):
                count_s, c = color.split(" ")
                count = int(count_s)
                if c not in self.max_seen or count > self.max_seen[c]:
                    self.max_seen[c] = count

    def get_max_seen_power(self) -> int:
        return self.max_seen["red"] * self.max_seen["green"] * self.max_seen["blue"]

    def check_valid(self) -> int:
        if (
            self.max_seen["red"] <= 12
            and self.max_seen["green"] <= 13
            and self.max_seen["blue"] <= 14
        ):
            return self.id
        return 0


class Day02:
    def __init__(self, input_filename: str = "day02.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    def parse_data(self, data: str) -> None:
        self.games = [Game(line) for line in data.rstrip().split("\n")]

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def part1(self) -> int:
        return sum([x.check_valid() for x in self.games])

    def part2(self) -> int:
        return sum([x.get_max_seen_power() for x in self.games])


if __name__ == "__main__":
    day = Day02()
    print(day.part1())
    print(day.part2())
