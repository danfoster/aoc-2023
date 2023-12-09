from day08 import Day08 as Day


class TestDay08:
    def test_part1_example(self) -> None:
        day = Day("day08_e1.txt")
        assert day.part1() == 2
        day = Day("day08_e2.txt")
        assert day.part1() == 6

    def test_part2_example(self) -> None:
        day = Day("day08_e3.txt")
        assert day.part2() == 6

    def test(self) -> None:
        day = Day("day08.txt")
        assert day.part1() == 16579
        assert day.part2() == 0
