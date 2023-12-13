from day13 import Day13 as Day


class TestDay13:
    def test_part1_example(self) -> None:
        day = Day("day13_e1.txt")
        assert day.part1() == 405

    def test_part2_example(self) -> None:
        day = Day("day13_e1.txt")
        assert day.part2() == 400

    def test(self) -> None:
        day = Day("day13.txt")
        assert day.part1() == 29165
        assert day.part2() == 1
