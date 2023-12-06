from day06 import Day06 as Day


class TestDay06:
    def test_part1_example(self) -> None:
        day = Day("day06_e1.txt")
        assert day.part1() == 288

    def test_part2_example(self) -> None:
        day = Day("day06_e1.txt")
        assert day.part2() == 71503

    def test(self) -> None:
        day = Day()
        assert day.part1() == 393120
        assert day.part2() == 36872656
