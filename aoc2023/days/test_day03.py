from aoc2023.days.day03 import Day03 as Day


class TestDay03:
    def test_part1_example(self) -> None:
        day = Day("day03_e1.txt")
        assert day.part1() == 4361

    def test_part2_example(self) -> None:
        day = Day("day03_e1.txt")
        day.part1()
        assert day.part2() == 467835

    def test(self) -> None:
        day = Day("day03.txt")
        assert day.part1() == 546312
        assert day.part2() == 87449461
