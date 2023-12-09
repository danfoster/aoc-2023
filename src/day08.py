from __future__ import annotations

import math
import os
from typing import Dict, List


class Node:
    left: Node | None
    right: Node | None
    label: str
    end: bool
    walked: bool
    steps_seen: List[int]

    def __init__(self, label: str) -> None:
        self.left = None
        self.right = None
        self.label = label
        self.walked = False
        self.end = label[2] == "Z"
        self.steps_seen = []

    def __repr__(self) -> str:
        return self.label


class Ghost:
    node: Node

    def __init__(self, starting_node: Node, directions: str):
        self.node = starting_node
        self.directions = directions
        self.directions_l = len(self.directions)

    def walk(self) -> int:
        steps = 0
        while True:
            assert steps < 100000

            if self.node.end:
                return steps

            if self.get_direction(steps):
                assert self.node.right is not None
                self.node = self.node.right
            else:
                assert self.node.left is not None
                self.node = self.node.left
            steps += 1

    def get_direction(self, step: int) -> bool:
        """
        False -> Left
        True -> Right
        """
        c = self.directions[step % self.directions_l]
        return c == "R"

    def print_mermaid(self) -> None:
        start_label: str = self.node.label
        steps: int = 0
        print(f"subgraph {start_label}")
        while True:
            assert steps < 100
            if self.get_direction(steps):
                assert self.node.right is not None
                print(f"    {self.node.label} -->|R| {self.node.right.label}")
                self.node = self.node.right
            else:
                assert self.node.left is not None
                print(f"    {self.node.label} -->|L| {self.node.left.label}")
                self.node = self.node.left
            steps += 1

            if self.node.label == start_label:
                break
            if self.node.end and self.node.walked:
                break
            self.node.walked = True
        print("end")


class Day08:
    directions: str
    nodes: Dict[str, Node]
    ghosts: List[Ghost]

    def __init__(self, input_filename: str = "day08.txt") -> None:
        self.nodes = {}
        self.ghosts = []
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        lines = iter(data.rstrip().split("\n"))
        self.directions = next(lines)
        next(lines)
        for line in lines:
            label = line[0:3]
            label_l = line[7:10]
            label_r = line[12:15]

            node = self.get_or_create_node(label)
            node.left = self.get_or_create_node(label_l)
            node.right = self.get_or_create_node(label_r)

            if label[2] == "A":
                self.ghosts.append(Ghost(node, self.directions))

    def get_or_create_node(self, label: str) -> Node:
        if label not in self.nodes:
            self.nodes[label] = Node(label)
        return self.nodes[label]

    def print_mermaid(self, start_node: str) -> None:
        node = self.get_or_create_node(start_node)
        print("flowchart TD")
        self._print_mermaid(node)

    def _print_mermaid(self, node: Node) -> None:
        if node.walked:
            return
        node.walked = True
        if node.left:
            print(f"    {node.label} -->|L| {node.left.label}")
            self._print_mermaid(node.left)
        if node.right:
            print(f"    {node.label} -->|R| {node.right.label}")
            self._print_mermaid(node.right)

    def reset_walked(self) -> None:
        for node in self.nodes.values():
            node.walked = False

    def part1(self) -> int:
        # self.print_mermaid("AAA")
        return Ghost(self.get_or_create_node("AAA"), self.directions).walk()

    def part2(self) -> int:
        distances: List[int] = []
        # print("graph TD")
        for ghost in self.ghosts:
            # ghost.print_mermaid()
            # self.reset_walked()
            distances.append(ghost.walk())

        # print(distances)
        return math.lcm(*distances)


if __name__ == "__main__":
    day = Day08()
    print(day.part1())
    print(day.part2())
