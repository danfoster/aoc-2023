
install:
    pip3 install -e .

run day:
    python3 -m aoc2023 {{day}}


test day:
    pytest aoc2023/days/test_day`printf "%02d" {{day}}`.py

new day:
    DAY=`printf "%02d" {{day}}` envsubst < templates/day.py > aoc2023/days/day`printf "%02d" {{day}}`.py
    DAY=`printf "%02d" {{day}}` envsubst < templates/test_day.py > aoc2023/days/test_day`printf "%02d" {{day}}`.py
