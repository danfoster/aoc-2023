
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

bench day:
    python3 -m cProfile -o output.prof src/bench.py {{day}} 
    snakeviz output.prof

docker_i:
    docker run -ti --rm \
        -v $(pwd):/code \
        -w /code \
        -e NUITKA_CACHE_DIR=/code/.cache \
        --user $(id -u):$(id -g) \
        aoc2023 bash
