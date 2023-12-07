import os
from collections import defaultdict
from functools import total_ordering
from typing import Dict, List


@total_ordering
class Hand:
    _type: int
    hand: str
    hand_as_score: List[int]
    bid: int

    def __init__(self, line: str):
        self.hand, bid = line.split()
        self.bid = int(bid)
        self.calc_hand_as_score()
        self.calc_type()

    def __repr__(self) -> str:
        return f"{self.hand}: {self._type}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return self._type == other._type and self.hand_as_score == other.hand_as_score

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        if self._type < other._type:
            return True
        if self._type > other._type:
            return False
        if self.hand_as_score < other.hand_as_score:
            return True
        return False

    def calc_hand_as_score(self, joker: bool = False) -> None:
        score_hand = []
        for c in self.hand:
            score_hand.append(self.card_to_strength(c, joker))
        self.hand_as_score = score_hand

    @staticmethod
    def card_to_strength(c: str, joker: bool) -> int:
        if joker:
            mapping = {
                "T": 10,
                "J": 1,
                "Q": 12,
                "K": 13,
                "A": 14,
            }
        else:
            mapping = {
                "T": 10,
                "J": 11,
                "Q": 12,
                "K": 13,
                "A": 14,
            }
        if c.isdigit():
            return int(c)
        return mapping[c]

    def calc_type(self, joker: bool = False) -> None:
        counts: Dict[str, int] = defaultdict(lambda: 0)
        jokers: int = 0
        for c in self.hand:
            if joker and c == "J":
                jokers += 1
                continue
            counts[c] += 1
        key = list(counts.values())
        key.sort(reverse=True)
        if joker:
            if len(key) > 0:
                key[0] += jokers
            else:
                key.append(jokers)
        if key == [5]:
            # Five of a kind
            self._type = 7
        elif key == [4, 1]:
            # Four of a kind
            self._type = 6
        elif key == [3, 2]:
            # Full House
            self._type = 5
        elif key == [3, 1, 1]:
            # Three of a kind
            self._type = 4
        elif key == [2, 2, 1]:
            # 2 Pair
            self._type = 3
        elif key == [2, 1, 1, 1]:
            # 1 Pair
            self._type = 2
        else:
            # High Card
            self._type = 1


class Day07:
    def __init__(self, input_filename: str = "day07.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data: List[Hand] = []
        for line in data.rstrip().split("\n"):
            self.data.append(Hand(line))

    def part1(self) -> int:
        ans: int = 0
        self.data.sort()
        for i, hand in enumerate(self.data):
            ans += (i + 1) * hand.bid
        return ans

    def part2(self) -> int:
        ans: int = 0
        for hand in self.data:
            hand.calc_hand_as_score(joker=True)
            hand.calc_type(joker=True)
        self.data.sort()
        for i, hand in enumerate(self.data):
            ans += (i + 1) * hand.bid
        return ans


if __name__ == "__main__":
    day = Day07()
    print(day.part1())
    print(day.part2())
