from day17 import Day17 as Day


class TestDay17:
    def test_part1_example(self) -> None:
        day = Day("day17_e1.txt")
        assert day.part1() == 102

    def test_part2_example(self) -> None:
        day = Day("day17_e1.txt")
        assert day.part2() == 94
        day = Day("day17_e2.txt")
        assert day.part2() == 71

    def test(self) -> None:
        day = Day("day17.txt")
        assert day.part1() == 1065
        assert day.part2() == 1249
