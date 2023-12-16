import os


class HASH:
    input: str
    value: int

    def __init__(self, input: str):
        self.input = input
        self.calc()

    def calc(self) -> None:
        value = 0
        for c in self.input:
            value += ord(c)
            value *= 17
            value = value % 256
        self.value = value

    def __repr__(self) -> str:
        return f"{self.input}: {self.value}"


class Day15:
    def __init__(self, input_filename: str = "day15.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data = [HASH(x) for x in data.rstrip().split(",")]

    def part1(self) -> int:
        return sum([x.value for x in self.data])

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day15()
    print(day.part1())
    print(day.part2())
