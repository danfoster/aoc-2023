import argparse
import importlib


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()
    day = args.day
    day_s = f"{day:02}"
    daymod = importlib.import_module(f"day{day_s}")
    dayclass = getattr(daymod, f"Day{day_s}")
    d = dayclass()
    # for i in range(0, 1000):
    #     d.part1()
    #     d.part2()
    print(d.part1())
    print(d.part2())


if __name__ == "__main__":
    main()
