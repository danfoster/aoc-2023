import os
from dataclasses import dataclass
from typing import Dict, List


class Node:
    children: List["Node"]
    label: str

    def __init__(self, label: str) -> None:
        self.children = []
        self.label = label

    def children_labels(self) -> List[str]:
        return [x.label for x in self.children]

    def add_child(self, child: "Node") -> None:
        self.children.append(child)
        child.parent_add_callback(self)

    def parent_add_callback(self, parent: "Node") -> None:
        pass

    def process(self, pulse: "Pulse") -> List["Pulse"]:
        raise NotImplementedError


class Broadcaster(Node):
    def process(self, pulse: "Pulse") -> List["Pulse"]:
        pulses: List[Pulse] = []
        for child in self.children:
            # print(f"{self.label} -{pulse.high}-> {child.label}")
            pulses.append(Pulse(self.label, child.label, pulse.high))
        return pulses


class NoOp(Node):
    def process(self, pulse: "Pulse") -> List["Pulse"]:
        return []


class FlipFlop(Node):
    state: bool

    def __init__(self, label: str) -> None:
        super().__init__(label)
        self.state = False

    def process(self, pulse: "Pulse") -> List["Pulse"]:
        pulses: List[Pulse] = []
        if pulse.high:
            return pulses

        self.state = not self.state
        for child in self.children:
            # print(f"{self.label} -{self.state}-> {child.label}")
            pulses.append(Pulse(self.label, child.label, self.state))
        return pulses


class Conjunction(Node):
    states: Dict[str, bool]

    def __init__(self, label: str) -> None:
        super().__init__(label)
        self.states = {}

    def process(self, pulse: "Pulse") -> List["Pulse"]:
        pulses: List[Pulse] = []
        self.states[pulse.source] = pulse.high

        state: bool = False
        for s in self.states.values():
            if not s:
                state = True
                break

        for child in self.children:
            # print(f"{self.label} -{state}-> {child.label}")
            pulses.append(Pulse(self.label, child.label, state))
        return pulses

    def parent_add_callback(self, parent: "Node") -> None:
        self.states[parent.label] = False


@dataclass
class Pulse:
    source: str
    dest: str
    high: bool


class Day20:
    nodes: Dict["str", Node]

    def __init__(self, input_filename: str = "day20.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        lines = data.rstrip().split("\n")
        self.nodes = {}
        for line in lines:
            label = line.split(" -> ", maxsplit=1)[0]
            if label.startswith("b"):
                self.nodes[label] = Broadcaster(label)
            elif label.startswith("%"):
                self.nodes[label[1:]] = FlipFlop(label[1:])
            elif label.startswith("&"):
                self.nodes[label[1:]] = Conjunction(label[1:])

        for line in lines:
            label, children = line.split(" -> ", maxsplit=1)
            if not label.startswith("b"):
                label = label[1:]
            for child in children.split(", "):
                if child not in self.nodes.keys():
                    self.nodes[child] = NoOp(child)
                self.nodes[label].add_child(self.nodes[child])

    def print_mermaid(self) -> None:
        print(f"graph TD")
        for key, value in self.nodes.items():
            for child in value.children_labels():
                print(f"  {key} --> {child}")

    def part1(self) -> int:
        lows: int = 0
        highs: int = 0
        # self.print_mermaid()
        for i in range(0, 1000):
            pulsequeue: List[Pulse] = [Pulse("aptly", "broadcaster", False)]
            lows += 1
            while len(pulsequeue) > 0:
                pulse = pulsequeue.pop(0)
                newpulses = self.nodes[pulse.dest].process(pulse)
                lows += sum([0 if x.high else 1 for x in newpulses])
                highs += sum([1 if x.high else 0 for x in newpulses])
                pulsequeue += newpulses
        return lows * highs

    def part2(self) -> int:
        ans: int = 0
        return ans


if __name__ == "__main__":
    day = Day20()
    print(day.part1())
    print(day.part2())
