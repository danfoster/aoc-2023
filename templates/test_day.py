from aoc2023.days.day${DAY} import Day${DAY} as Day


class TestDay${DAY}:
    def test_part1_example(self) -> None:
        day = Day("day${DAY}_e1.txt")
        assert day.part1() == None
        

    def test_part2_example(self) -> None:
        day = Day("day${DAY}_e1.txt")
        assert day.part2() == None

    def test(self) -> None:
        day = Day("day${DAY}.txt")
        assert day.part1() == None
        assert day.part2() == None
