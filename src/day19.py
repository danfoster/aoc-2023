import os
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Rule:
    var: str
    condition: bool
    value: int
    dest: str


CONDITION_MAPPING: Dict[str, bool] = {"<": False, ">": True}


class Workflow:
    rules: List[Rule]
    default: str

    def __init__(self, rules: List[str]):
        self.rules = []
        for rule in rules[:-1]:
            part, dest = rule.split(":", maxsplit=1)
            self.rules.append(
                Rule(part[0], CONDITION_MAPPING[part[1]], int(part[2:]), dest)
            )
        self.default = rules[-1]

    def __repr__(self) -> str:
        return str(self.rules)

    def match(self, part: "Part") -> str:
        for rule in self.rules:
            if not rule.condition:
                if getattr(part, rule.var) < rule.value:
                    return rule.dest
            else:
                if getattr(part, rule.var) > rule.value:
                    return rule.dest
        return self.default


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def process(self, workflows: Dict[str, Workflow]) -> bool:
        workflow_label = "in"
        while workflow_label not in ["R", "A"]:
            print(f"{workflow_label} --> ", end="")
            workflow = workflows[workflow_label]
            workflow_label = workflow.match(self)
        print(workflow_label)

        return workflow_label == "A"

    def totalrating(self) -> int:
        return self.x + self.m + self.a + self.s


class Day19:
    workflows: Dict[str, Workflow]
    parts: List[Part]

    def __init__(self, input_filename: str = "day19.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.workflows = {}
        lines = iter(data.rstrip().split("\n"))
        for line in lines:
            if line == "":
                break
            label, rest = line.split("{", maxsplit=1)
            self.workflows[label] = Workflow(rest[:-1].split(","))

        self.parts = []
        for line in lines:
            self.parts.append(Part(*[int(x[2:]) for x in line[1:-1].split(",")]))

    def part1(self) -> int:
        ans: int = 0
        for part in self.parts:
            if part.process(self.workflows):
                ans += part.totalrating()
        return ans

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day19()
    print(day.part1())
    print(day.part2())
