from day14 import Day14 as Day


class TestDay14:
    def test_part1_example(self) -> None:
        day = Day("day14_e1.txt")
        assert day.part1() == 136

    def test_part2_example(self) -> None:
        day = Day("day14_e1.txt")
        assert day.part2() == 64

    def test(self) -> None:
        day = Day("day14.txt")
        assert day.part1() == 109665
        assert day.part2() == 1
