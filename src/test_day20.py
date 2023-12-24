from day20 import Day20 as Day


class TestDay20:
    def test_part1_example(self) -> None:
        day = Day("day20_e1.txt")
        assert day.part1() == 32000000
        day = Day("day20_e2.txt")
        assert day.part1() == 11687500

    def test(self) -> None:
        day = Day("day20.txt")
        assert day.part1() == 731517480
        assert day.part2() == 244178746156661
