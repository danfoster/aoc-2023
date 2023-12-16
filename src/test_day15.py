from day15 import Day15 as Day


class TestDay15:
    def test_part1_example(self) -> None:
        day = Day("day15_e1.txt")
        assert day.part1() == 1320

    def test_part2_example(self) -> None:
        day = Day("day15_e1.txt")
        assert day.part2() == 1

    def test(self) -> None:
        day = Day("day15.txt")
        assert day.part1() == 1
        assert day.part2() == 1
