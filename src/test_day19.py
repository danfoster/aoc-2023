from day19 import Day19 as Day


class TestDay19:
    def test_part1_example(self) -> None:
        day = Day("day19_e1.txt")
        assert day.part1() == 19114

    def test_part2_example(self) -> None:
        day = Day("day19_e1.txt")
        assert day.part2() == 1

    def test(self) -> None:
        day = Day("day19.txt")
        assert day.part1() == 1
        assert day.part2() == 1
