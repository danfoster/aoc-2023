import importlib

import click


@click.command()
@click.argument("day", type=int)
def main(day: int) -> None:
    day_s = f"{day:02}"
    daymod = importlib.import_module(f".days.day{day_s}", "aoc2023")
    dayclass = getattr(daymod, f"Day{day_s}")
    d = dayclass()
    print(d.part1())
    print(d.part2())


if __name__ == "__main__":
    main()
