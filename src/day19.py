import os
from collections import defaultdict
from copy import copy
from dataclasses import dataclass
from typing import DefaultDict, Dict, List

CONDITION_MAPPING: Dict[str, bool] = {"<": False, ">": True}


@dataclass
class Rule:
    var: str
    condition: bool
    value: int
    dest: str


@dataclass
class Range:
    a: int
    b: int

    def len(self) -> int:
        return abs(self.b - self.a) + 1


@dataclass
class PartRange:
    x: Range
    m: Range
    a: Range
    s: Range

    def size(self) -> int:
        return self.x.len() * self.m.len() * self.a.len() * self.s.len()


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

    def totalrating(self) -> int:
        return self.x + self.m + self.a + self.s


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

    def match_part(self, part: "Part") -> str:
        for rule in self.rules:
            if not rule.condition:
                if getattr(part, rule.var) < rule.value:
                    return rule.dest
            else:
                if getattr(part, rule.var) > rule.value:
                    return rule.dest
        return self.default

    def match_partrange(
        self, partrange: "PartRange"
    ) -> DefaultDict[str, List["PartRange"]]:
        newmapping: DefaultDict[str, List["PartRange"]] = defaultdict(list)
        for rule in self.rules:
            r = getattr(partrange, rule.var)
            if not rule.condition:
                # Checking <
                if r.a >= rule.value:
                    # The whole range doesn't match
                    continue
                elif r.b <= rule.value:
                    # The whole range matches
                    newmapping[rule.dest].append(partrange)
                    return newmapping
                else:
                    # Split the range
                    newpartrange = copy(partrange)
                    setattr(
                        newpartrange,
                        rule.var,
                        Range(getattr(partrange, rule.var).a, rule.value - 1),
                    )
                    setattr(
                        partrange,
                        rule.var,
                        Range(rule.value, getattr(partrange, rule.var).b),
                    )
                    newmapping[rule.dest].append(newpartrange)
            else:
                # Checking >
                if r.a >= rule.value:
                    # The whole range matches
                    newmapping[rule.dest].append(partrange)
                    return newmapping
                elif r.b <= rule.value:
                    # The whole range doesn't match
                    continue
                else:
                    # Split the range
                    newpartrange = copy(partrange)
                    setattr(
                        newpartrange,
                        rule.var,
                        Range(rule.value + 1, getattr(partrange, rule.var).b),
                    )
                    setattr(
                        partrange,
                        rule.var,
                        Range(getattr(partrange, rule.var).a, rule.value),
                    )
                    newmapping[rule.dest].append(newpartrange)

        newmapping[self.default].append(partrange)
        return newmapping

    def process_partranges(
        self, partranges: List["PartRange"]
    ) -> Dict[str, List["PartRange"]]:
        newparts: Dict[str, List["PartRange"]] = {}
        for partrange in partranges:
            prl = self.match_partrange(partrange)
            newparts.update(prl)
        return newparts

    def process_parts(self, parts: List[Part]) -> Dict[str, List[Part]]:
        newparts: DefaultDict[str, List["Part"]] = defaultdict(list)
        for part in parts:
            label = self.match_part(part)
            newparts[label].append(part)
        return newparts


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
        parts: DefaultDict[str, List[Part]] = defaultdict(list)
        parts["in"] = self.parts
        accepted: List[Part] = []
        while parts:
            label = next(iter(parts.keys()))
            pl = parts.pop(label)
            newparts = self.workflows[label].process_parts(pl)
            newparts.pop("R", None)
            accepted += newparts.pop("A", [])
            parts.update(newparts)

        return sum([x.totalrating() for x in accepted])

    def part2(self) -> int:
        parts: DefaultDict[str, List[PartRange]] = defaultdict(list)
        parts["in"].append(
            PartRange(Range(1, 4000), Range(1, 4000), Range(1, 4000), Range(1, 4000))
        )
        accepted: List[PartRange] = []
        while parts:
            label = next(iter(parts.keys()))
            pl = parts.pop(label)
            newparts = self.workflows[label].process_partranges(pl)
            parts.update(newparts)
            parts.pop("R", None)
            accepted += parts.pop("A", [])
        return sum([x.size() for x in accepted])


if __name__ == "__main__":
    day = Day19()
    print(day.part1())
    print(day.part2())
