from math import factorial
from typing import List

from ..utils.day import Day
from ..utils.io import read_file


class Card:
    winning_nums: List[str]
    nums: List[str]
    winning_count: int

    def __init__(self, line: str):
        parts = line.split(": ")
        winning, nums = parts[1].split(" | ")
        self.winning_nums = winning.split()
        self.nums = nums.split()
        # print(self.winning_nums, self.nums)

    def calc_winning_value(self) -> None:
        self.winning_count = 0
        for num in self.nums:
            if num in self.winning_nums:
                self.winning_count += 1

    def get_score(self) -> int:
        if self.winning_count > 0:
            return 1 << (self.winning_count - 1)
        return 0


class Day04(Day):
    def __init__(self, input_filename: str = "day04.txt") -> None:
        self.data = self.parse_cards(self.parse_data(read_file(input_filename)))

    def parse_cards(self, lines: List[str]) -> List[Card]:
        data: List[Card] = []
        for line in lines:
            data.append(Card(line))
        return data

    def part1(self) -> str:
        sum = 0
        for card in self.data:
            card.calc_winning_value()
            sum += card.get_score()
        return str(sum)

    def part2(self) -> str:
        return ""
