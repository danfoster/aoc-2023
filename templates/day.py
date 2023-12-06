import os


class Day${DAY}:
    def __init__(self, input_filename: str = "day${DAY}.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def get_input_dir() -> str:
        path = os.path.abspath(__file__)
        path = f"{path}/../../../inputs/"
        return os.path.abspath(path)

    @classmethod
    def read_file(cls, filename: str) -> str:
        with open(os.path.join(cls.get_input_dir(), filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")

    def part1(self) -> int:
        ans: int = 0
        return ans

    def part2(self) -> int:
        ans: int = 0
        return ans
