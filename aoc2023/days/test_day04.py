from aoc2023.days.day04 import Day04 as Day

DAY = "04"


class TestDay04:
    def test_part1_example(self) -> None:
        day = Day(f"day{DAY}_e1.txt")
        assert day.part1() == "13"

    def test_part2_example(self) -> None:
        day = Day(f"day{DAY}_e2.txt")
        assert day.part2() == "281"

    def test(self) -> None:
        day = Day(f"day{DAY}.txt")
        assert day.part1() == "55108"
        assert day.part2() == "56324"
