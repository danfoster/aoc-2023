import os
from typing import List, Set


class Card:
    winning_nums: Set[str]
    nums: Set[str]
    winning_count: int
    count: int

    def __init__(self, line: str):
        parts = line.split(": ", maxsplit=1)
        winning, nums = parts[1].split(" | ")
        self.winning_nums = set(winning.split())
        self.nums = set(nums.split())
        # print(self.winning_nums, self.nums)
        self.count = 1

    def calc_winning_value(self) -> None:
        self.winning_count = len(self.winning_nums.intersection(self.nums))

    def get_score(self) -> int:
        if self.winning_count > 0:
            return 1 << (self.winning_count - 1)
        return 0


class Day04:
    def __init__(self, input_filename: str = "day04.txt") -> None:
        self.parse_data(self.read_file(input_filename))
        self.cards = self.parse_cards()

    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_cards(self) -> List[Card]:
        data: List[Card] = []
        for line in self.data:
            data.append(Card(line))
        return data

    def part1(self) -> int:
        sum = 0
        for card in self.cards:
            card.calc_winning_value()
            sum += card.get_score()
        return sum

    def part2(self) -> int:
        sum = 0
        for k, card in enumerate(self.cards):
            for i in range(k + 1, k + card.winning_count + 1):
                self.cards[i].count += 1 * card.count
            sum += card.count
            # print(f"[{k+1}] {card.count} {card.winning_count}")
        return sum


if __name__ == "__main__":
    day = Day04()
    print(day.part1())
    print(day.part2())
