from aoc2023.days.day01 import Day01 as Day

DAY = "01"


class TestDay01:
    def test_part1_example(self) -> None:
        day = Day(f"day{DAY}_e1.txt")
        assert day.part1() == "142"

    def test_part2_example(self) -> None:
        day = Day(f"day{DAY}_e2.txt")
        day.part1()
        assert day.part2() == "281"

    def test(self) -> None:
        day = Day(f"day{DAY}.txt")
        assert day.part1() == "55108"
        assert day.part2() == "56324"
