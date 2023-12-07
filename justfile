
install:
    pip3 install -e .

run day:
    python3 src/day{{day}}.py


test day:
    pytest src/test_day{{day}}.py

test_p1 day:
    pytest src/test_day{{day}}.py::TestDay{{day}}::test_part1_example

test_p2 day:
    pytest src/test_day{{day}}.py::TestDay{{day}}::test_part2_example


new day:
    DAY={{day}} envsubst < templates/day.py > src/day{{day}}.py
    DAY={{day}} envsubst < templates/test_day.py > src/test_day{{day}}.py

