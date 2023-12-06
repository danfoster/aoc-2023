from day04 import Day04 as Day


class TestDay04:
    def test_part1_example(self) -> None:
        day = Day("day04_e1.txt")
        assert day.part1() == 13

    def test_part2_example(self) -> None:
        day = Day("day04_e1.txt")
        day.part1()
        assert day.part2() == 30

    def test(self) -> None:
        day = Day("day04.txt")
        assert day.part1() == 28750
        assert day.part2() == 10212704
