from day18 import Day18 as Day


class TestDay18:
    def test_part1_example(self) -> None:
        day = Day("day18_e1.txt")
        assert day.part1() == 62

    def test_part2_example(self) -> None:
        day = Day("day18_e1.txt")
        assert day.part2() == 1

    def test(self) -> None:
        day = Day("day18.txt")
        assert day.part1() == 1
        assert day.part2() == 1
