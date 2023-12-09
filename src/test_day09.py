from day09 import Day09 as Day


class TestDay09:
    def test_part1_example(self) -> None:
        day = Day("day09_e1.txt")
        assert day.part1() == 114

    def test_part2_example(self) -> None:
        day = Day("day09_e1.txt")
        day.part1()
        assert day.part2() == 2

    def test(self) -> None:
        day = Day("day09.txt")
        assert day.part1() == 2105961943
        assert day.part2() == 1019
