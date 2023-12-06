from day02 import Day02 as Day


class TestDay02:
    def test_part1_example(self) -> None:
        day = Day("day02_e1.txt")
        assert day.part1() == 8

    def test_part2_example(self) -> None:
        day = Day("day02_e1.txt")
        assert day.part2() == 2286

    def test(self) -> None:
        day = Day("day02.txt")
        assert day.part1() == 2617
        assert day.part2() == 59795
