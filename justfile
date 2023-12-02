
install:
    pip3 install -e .

run day:
    python3 -m aoc2023 {{day}}


test day:
    pytest aoc2023/days/test_day`printf "%02d" {{day}}`.py

test_p1 day:
    pytest aoc2023/days/test_day`printf "%02d" {{day}}`.py::TestDay`printf "%02d" {{day}}`::test_part1_example

test_p2 day:
    pytest aoc2023/days/test_day`printf "%02d" {{day}}`.py::TestDay`printf "%02d" {{day}}`::test_part2_example


new day:
    DAY=`printf "%02d" {{day}}` envsubst < templates/day.py > aoc2023/days/day`printf "%02d" {{day}}`.py
    DAY=`printf "%02d" {{day}}` envsubst < templates/test_day.py > aoc2023/days/test_day`printf "%02d" {{day}}`.py
