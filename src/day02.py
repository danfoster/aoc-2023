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

    def check_valid(self) -> bool:
        return (
            self.max_seen["red"] <= 12
            and self.max_seen["green"] <= 13
            and self.max_seen["blue"] <= 14
        )


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
        sum = 0
        for game in self.games:
            if game.check_valid():
                sum += game.id
        return sum

    def part2(self) -> int:
        sum: int = 0
        for game in self.games:
            sum += game.get_max_seen_power()
        return sum


if __name__ == "__main__":
    day = Day02()
    print(day.part1())
    print(day.part2())
