from aoc2023.days.day02 import Day02 as Day

DAY = "02"


class TestDay02:
    def test_part1_example(self) -> None:
        day = Day(f"day{DAY}_e1.txt")
        assert day.part1() == "8"

    def test_part2_example(self) -> None:
        day = Day(f"day{DAY}_e2.txt")
        assert day.part2() == "2286"

    def test(self) -> None:
        day = Day(f"day{DAY}.txt")
        assert day.part1() == "2617"
        assert day.part2() == "56324"
