from day11 import Day11 as Day


class TestDay11:
    def test_part1_example(self) -> None:
        day = Day("day11_e1.txt")
        assert day.part1() == 374

    def test_part2_example(self) -> None:
        day = Day("day11_e1.txt")
        assert day.part2() == 1

    def test(self) -> None:
        day = Day("day11.txt")
        assert day.part1() == 1
        assert day.part2() == 1
