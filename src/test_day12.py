from day12 import Day12 as Day


class TestDay12:
    def test_part1_example(self) -> None:
        day = Day("day12_e1.txt")
        assert day.part1() == 21

    def test_part2_example(self) -> None:
        day = Day("day12_e1.txt")
        assert day.part2() == 525152

    def test(self) -> None:
        day = Day("day12.txt")
        assert day.part1() == 7110
        assert day.part2() == 1566786613613
