from day11 import Day11 as Day


class TestDay11:
    def test_part1_example(self) -> None:
        day = Day("day11_e1.txt")
        assert day.part1() == 374

    def test_part2_example(self) -> None:
        day = Day("day11_e1.txt")
        assert day.part2(multiplier=10) == 1030
        day.parse_data()
        assert day.part2(multiplier=100) == 8410

    def test(self) -> None:
        day = Day("day11.txt")
        assert day.part1() == 9795148
        day.parse_data()
        assert day.part2() == 650672493820
