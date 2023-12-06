import os


class Day${DAY}:
    def __init__(self, input_filename: str = "day${DAY}.txt") -> None:
        self.parse_data(self.read_file(input_filename))


    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()


    def parse_data(self, data: str) -> None:
        self.data = data.rstrip().split("\n")

    def part1(self) -> int:
        ans: int = 0
        return ans

    def part2(self) -> int:
        ans: int = 0
        return ans



if __name__ == "__main__":
    day = Day${DAY}()
    print(day.part1())
    print(day.part2())
