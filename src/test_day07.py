from day07 import Day07 as Day


class TestDay07:
    def test_part1_example(self) -> None:
        day = Day("day07_e1.txt")
        assert day.part1() == 6440

    def test_part2_example(self) -> None:
        day = Day("day07_e1.txt")
        assert day.part2() == 5905

    def test(self) -> None:
        day = Day("day07.txt")
        assert day.part1() == None
        assert day.part2() == None
