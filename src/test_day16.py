from day16 import Day16 as Day


class TestDay16:
    def test_part1_example(self) -> None:
        day = Day("day16_e1.txt")
        assert day.part1() == 46

    def test_part2_example(self) -> None:
        day = Day("day16_e1.txt")
        assert day.part2() == 51

    def test(self) -> None:
        day = Day("day16.txt")
        assert day.part1() == 7870
        assert day.part2() == 1
