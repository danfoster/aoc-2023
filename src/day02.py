import os
import re
from typing import Dict


class Game:
    def __init__(self, line: str):
        matches = re.match("Game ([0-9]+): (.*)", line)
        assert matches is not None
        self.id = int(matches.group(1))
        self.max_seen: Dict[str, int] = {}

        for part in matches.group(2).split("; "):
            for color in part.split(", "):
                count, c = color.split(" ")
                count = int(count)
                if c not in self.max_seen or count > self.max_seen[c]:
                    self.max_seen[c] = count

    def get_max_seen_power(self) -> int:
        return self.max_seen["red"] * self.max_seen["green"] * self.max_seen["blue"]

    def check_valid(self, conditions: Dict[str, int]) -> int:
        ckeys = conditions.keys()
        for color, value in self.max_seen.items():
            if color not in ckeys:
                return 0
            if value > conditions[color]:
                return 0
        return self.id


class Day02:
    def __init__(self, input_filename: str = "day02.txt") -> None:
        self.parse_data(self.read_file(input_filename))
        self.games = []
        for line in self.data:
            self.games.append(Game(line))

    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def part1(self) -> int:
        # 12 red cubes, 13 green cubes, and 14 blue cubes?
        conditions = {"red": 12, "green": 13, "blue": 14}
        sum = 0
        for game in self.games:
            sum += game.check_valid(conditions)
        return sum

    def part2(self) -> int:
        sum = 0
        for game in self.games:
            sum += game.get_max_seen_power()
        return sum
