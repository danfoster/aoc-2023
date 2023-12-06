import os
from collections import defaultdict
from typing import DefaultDict, List


class Number:
    value: str
    y: int
    x1: int
    x2: int

    def __init__(self) -> None:
        self.value = ""

    def __repr__(self) -> str:
        return f"[({self.x1}-{self.x2}),{self.y}] {self.value}"

    def add_char(self, c: str, x: int, y: int) -> None:
        if not self.value:
            self.x1 = x
            self.y = y
            self.value = c
        else:
            self.value += c

    def finish(self, x: int) -> bool:
        if not self.value:
            return False

        self.x2 = x - 1
        return True

    def get(self) -> int:
        return int(self.value)


class Symbol:
    x: int
    y: int
    symbol: str
    ratio: int
    numbercount: int

    def __init__(self, x: int, y: int, s: str):
        self.x = x
        self.y = y
        self.symbol = s
        self.ratio = 1
        self.numbercount = 0

    def add_ratio(self, number: Number) -> None:
        if self.symbol == "*":
            self.ratio *= number.get()
            self.numbercount += 1

    def get_ratio(self) -> int:
        if self.symbol == "*" and self.numbercount > 1:
            return self.ratio
        return 0


class Schematic:
    def __init__(self, data: List[str]):
        self.symbols: DefaultDict[int, List[Symbol]] = defaultdict(list)
        self.numbers: List[Number] = []

        self.read_data(data)

    def read_data(self, data: List[str]) -> None:
        number = Number()
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                if c == ".":
                    if number.finish(x):
                        self.numbers.append(number)
                        number = Number()
                elif c.isdigit():
                    number.add_char(c, x, y)
                else:
                    if number.finish(x):
                        self.numbers.append(number)
                        number = Number()
                    self.symbols[y].append(Symbol(x, y, c))
            if number.finish(x):
                self.numbers.append(number)
                number = Number()
        self.rows = y

    def print_numbers(self) -> None:
        for i in self.numbers:
            print(i)

    def print_symbols(self) -> None:
        for i in self.symbols:
            print(f"{i}: {self.symbols[i]}")

    def is_number_by_symbol(self, number: Number) -> bool:
        nextto = False
        for symbol in self.symbols[number.y]:
            if symbol.x == number.x1 - 1 or symbol.x == number.x2 + 1:
                symbol.add_ratio(number)
                nextto = True
        if number.y - 1 >= 0:
            for symbol in self.symbols[number.y - 1]:
                if symbol.x >= number.x1 - 1 and symbol.x <= number.x2 + 1:
                    symbol.add_ratio(number)
                    nextto = True
        if number.y + 1 < self.rows:
            for symbol in self.symbols[number.y + 1]:
                if symbol.x >= number.x1 - 1 and symbol.x <= number.x2 + 1:
                    symbol.add_ratio(number)
                    nextto = True
        return nextto


class Day03:
    def __init__(self, input_filename: str = "day03.txt") -> None:
        self.parse_data(self.read_file(input_filename))
        self.schematic = Schematic(self.data)

    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")

    @staticmethod
    def get_input_dir() -> str:
        path = os.path.abspath(__file__)
        path = f"{path}/../../../inputs/"
        return os.path.abspath(path)

    @classmethod
    def read_file(cls, filename: str) -> str:
        with open(os.path.join(cls.get_input_dir(), filename), "r") as file:
            return file.read()

    def part1(self) -> int:
        sum = 0
        for number in self.schematic.numbers:
            valid = self.schematic.is_number_by_symbol(number)
            if valid:
                sum += number.get()
        return sum

    def part2(self) -> int:
        sum = 0
        for row in self.schematic.symbols.values():
            for symbol in row:
                if symbol.symbol == "*":
                    sum += symbol.get_ratio()
        return sum
