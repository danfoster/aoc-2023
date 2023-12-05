from aoc2023.days.day05 import Day05 as Day

DAY = "05"


class TestDay05:
    def test_part1_example(self) -> None:
        day = Day(f"day{DAY}_e1.txt")
        assert day.part1() == "35"

    def test_part2_example(self) -> None:
        day = Day(f"day{DAY}_e2.txt")
        assert day.part2() == "46"

    def test(self) -> None:
        day = Day(f"day{DAY}.txt")
        assert day.part1() == ""
        assert day.part2() == ""
