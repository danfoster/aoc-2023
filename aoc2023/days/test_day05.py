from aoc2023.days.day05 import Day05 as Day


class TestDay05:
    def test_part1_example(self) -> None:
        day = Day("day05_e1.txt")
        assert day.part1() == 35

    def test_part2_example(self) -> None:
        day = Day("day05_e1.txt")
        assert day.part2() == 46

    def test(self) -> None:
        day = Day("day05.txt")
        assert day.part1() == 226172555
        assert day.part2() == 47909639
