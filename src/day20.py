import os
from dataclasses import dataclass
from math import lcm
from typing import Dict, List, Tuple


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

    def graph_key(self) -> str:
        return self.label

    def __repr__(self) -> str:
        key = ""
        if isinstance(self, FlipFlop):
            key = "%"
        elif isinstance(self, Conjunction):
            key = "&"

        return f"{key}{self.label}"


class Broadcaster(Node):
    def process(self, pulse: "Pulse") -> List["Pulse"]:
        pulses: List[Pulse] = []
        for child in self.children:
            # print(f"{self.label} -{pulse.high}-> {child.label}")
            pulses.append(Pulse(self.label, child.label, pulse.high))
        return pulses

    def graph_key(self) -> str:
        return f"{self.label} [shape=point]"


class NoOp(Node):
    def process(self, pulse: "Pulse") -> List["Pulse"]:
        return []

    def graph_key(self) -> str:
        return f"{self.label} [shape=point]"


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

    def graph_key(self) -> str:
        return f"{self.label} [shape=diamond]"


class Conjunction(Node):
    states: Dict[str, bool]

    def __init__(self, label: str) -> None:
        super().__init__(label)
        self.states = {}

    def output(self) -> bool:
        for s in self.states.values():
            if not s:
                return True
        return False

    def process(self, pulse: "Pulse") -> List["Pulse"]:
        pulses: List[Pulse] = []
        self.states[pulse.source] = pulse.high

        state = self.output()
        for child in self.children:
            # print(f"{self.label} -{state}-> {child.label}")
            pulses.append(Pulse(self.label, child.label, state))
        return pulses

    def parent_add_callback(self, parent: "Node") -> None:
        self.states[parent.label] = False

    def graph_key(self) -> str:
        shape = "box"
        if len(self.states) == 1:
            shape = "invtriangle"
        return f"{self.label} [shape={shape}]"


@dataclass
class Pulse:
    source: str
    dest: str
    high: bool


class Day20:
    nodes: Dict["str", Node]

    def __init__(self, input_filename: str = "day20.txt") -> None:
        self.rawdata = self.read_file(input_filename)
        self.parse_data(self.rawdata)

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

    def draw_graph(self) -> None:
        with open("graph.dot", "w") as f:
            print("digraph G {", file=f)
            for key, value in self.nodes.items():
                nodelabel = self.nodes[key].graph_key()
                print(f"  {nodelabel};", file=f)
                for child in value.children_labels():
                    print(f"  {key} -> {child};", file=f)
            print("}", file=f)

    def find_keys(self) -> List[Node]:
        return self.nodes["broadcaster"].children

    def get_flipflopchain(self, node: Node | None) -> List[bool]:
        bitmask: List[bool] = []
        while node:
            newnode = None
            bit = False
            for child in node.children:
                if isinstance(child, FlipFlop):
                    newnode = child
                elif isinstance(child, Conjunction):
                    bit = True
            node = newnode
            bitmask.append(bit)
        return bitmask

    @staticmethod
    def bitmasktoint(bitmask: List[bool]) -> int:
        total: int = 0
        for i, bit in enumerate(bitmask):
            if bit:
                total += 1 << i
        return total

    def part1(self) -> int:
        lows: int = 0
        highs: int = 0

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
        # self.draw_graph()
        values: List[int] = []
        for key in self.find_keys():
            bitmask = self.get_flipflopchain(key)
            values.append(self.bitmasktoint(bitmask))
        return lcm(*values)


if __name__ == "__main__":
    day = Day20()
    print(day.part1())
    day.parse_data(day.rawdata)
    print(day.part2())
