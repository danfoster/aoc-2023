from day10 import Day10 as Day


class TestDay10:
    def test_part1_example(self) -> None:
        day = Day("day10_e1.txt")
        assert day.part1() == 4
        day = Day("day10_e2.txt")
        assert day.part1() == 8

    def test_part2_example(self) -> None:
        day = Day("day10_e1.txt")
        assert day.part2() == 0

    def test(self) -> None:
        day = Day("day10.txt")
        assert day.part1() == 6649
        assert day.part2() == 0
