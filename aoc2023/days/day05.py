from dataclasses import dataclass
from functools import total_ordering
from pprint import pprint
from typing import Dict, List

from ..utils.day import Day
from ..utils.io import read_file

# class Node:
#     id: int
#     target: int

#     def __repr__(self) -> str:
#         return f"[{self.id}]"

#     def __init__(self, id: int):
#         self.id = id
#         self.target = id


# class Nodes:
#     def __init__(self):
#         self.mappings = {}

#     def add_mapping(self, source, dest):
#         self.mapping[source] = dest


@dataclass
@total_ordering
class Range:
    start: int
    end: int

    def valid(self) -> bool:
        return self.end > self.start

    def __repr__(self) -> str:
        return f"{self.start}-{self.end}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Range):
            return NotImplemented
        return self.start == other.start

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Range):
            return NotImplemented
        return self.start < other.start


class Mapping:
    def __init__(self, dest: int, source: int, size: int):
        self.dest = dest
        self.source = source
        self.size = size
        self.diff = self.dest - self.source

    def __repr__(self) -> str:
        return (
            f"{self.source}-{self.source+self.size-1}"
            f"-> {self.dest}-{self.dest+self.size-1}"
            f" ({self.diff})"
        )

    def map(self, n: int) -> (int, bool):
        if n >= self.source and n < self.source + self.size:
            # print(self)
            # print(f"** {self.diff}")
            return n + self.diff, True
        return n, False

    def map_range(self, r: Range) -> (List[Range], List[Range]):
        unmapped_ranges: List[Range] = []
        mapped_ranges: List[Range] = []

        before = Range(r.start, min(self.source, r.end))
        middle = Range(max(r.start, self.source), min(self.source + self.size, r.end))
        end = Range(max(self.source + self.size, r.start), r.end)
        if before.valid():
            unmapped_ranges.append(before)
        if middle.valid():
            middle.start += self.diff
            middle.end += self.diff
            mapped_ranges.append(middle)
        if end.valid():
            unmapped_ranges.append(end)

        return mapped_ranges, unmapped_ranges


class Day05(Day):
    def __init__(self, input_filename: str = "day05.txt") -> None:
        self.parse_data(read_file(input_filename))

    def parse_data(self, data: str) -> None:
        super().parse_data(data)

        self.seeds: List[int] = [int(x) for x in self.data[0][7:].split()]
        self.nodes: Dict[int, int] = {}
        self.mappings: List[List[Mapping]] = []
        lines = iter(self.data[2:])
        for line in lines:
            mappings: List[Mapping] = []
            for line in lines:
                if line == "":
                    break
                mappings.append(Mapping(*[int(x) for x in line.split()]))
            self.mappings.append(mappings)

    def update_mapping(self, dest: int, source: int, size: int) -> None:
        for n in range(size):
            self.nodes[source + n] = dest + n

    def part1(self) -> str:
        locations: List[int] = []
        for seed in self.seeds:
            # print("-----
            # ")
            for mappings in self.mappings:
                # print(seed)
                for mapping in mappings:
                    seed, done = mapping.map(seed)
                    if done:
                        break
            locations.append(seed)
        return str(min(locations))

    def part2(self) -> str:
        locations: List[int] = []
        for range in [
            Range(x, x + i) for (x, i) in zip(self.seeds[::2], self.seeds[1::2])
        ]:
            unmapped_ranges = [range]

            for mappings in self.mappings:
                mapped_ranges: List[Range] = []
                for mapping in mappings:
                    unmapped_ranges_t: List[Range] = []
                    for umr in unmapped_ranges:
                        mrt, umrt = mapping.map_range(umr)
                        unmapped_ranges_t += umrt
                        mapped_ranges += mrt
                    unmapped_ranges = unmapped_ranges_t
                unmapped_ranges = mapped_ranges + unmapped_ranges
            locations.append(min(unmapped_ranges).start)
        return str(min(locations))
