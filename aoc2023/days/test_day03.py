from aoc2023.days.day03 import Day03 as Day

DAY = "03"


class TestDay03:
    def test_part1_example(self) -> None:
        day = Day(f"day{DAY}_e1.txt")
        assert day.part1() == "4361"

    def test_part2_example(self) -> None:
        day = Day(f"day{DAY}_e2.txt")
        day.part1()
        assert day.part2() == "467835"

    def test(self) -> None:
        day = Day(f"day{DAY}.txt")
        assert day.part1() == "55108"
        assert day.part2() == "56324"
