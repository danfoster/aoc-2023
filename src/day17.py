import heapq
import os
from dataclasses import dataclass
from functools import total_ordering
from typing import Dict, Generic, Iterable, List, Optional, Tuple, TypeVar

T = TypeVar("T")

# north = 0
# east = 1
# south = 2
# west = 3
VECTORS: Dict[int, List[int]] = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self.elements: list[tuple[int, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: int) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


@dataclass
@total_ordering
class GridPoint:
    x: int
    y: int
    dir: int
    speed: int

    def in_bounds(self, width: int, height: int) -> bool:
        if self.x >= 0 and self.y >= 0 and self.x < width and self.y < height:
            return True
        return False

    def __key(self) -> Tuple[int, int, int, int]:
        return (self.x, self.y, self.dir, self.speed)

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other: object) -> bool:
        if isinstance(other, GridPoint):
            return self.__key() == other.__key()
        elif isinstance(other, tuple):
            return bool(self.x == other[0] and self.y == other[1])
        raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        if isinstance(other, GridPoint):
            return (self.x + self.y) < (other.x + other.y)
        raise NotImplementedError


class Grid:
    def __init__(self, input: List[str], maxspeed: int = 3, minspeed: int = 0):
        self.grid = [[int(x) for x in line] for line in input]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.maxspeed = maxspeed
        self.minspeed = minspeed

    def draw_path(self, start: GridPoint, end: GridPoint) -> None:
        path = self.reconstruct_path(start, end)
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == start:
                    print("S", end="")
                elif (x, y) == end:
                    print("G", end="")
                elif (x, y) in path:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def reconstruct_path(
        self, start: GridPoint, goal: GridPoint
    ) -> list[Tuple[int, int]]:
        current: GridPoint = goal
        path: list[Tuple[int, int]] = []
        if goal not in self.came_from:  # no path was found
            return []
        while current != start:
            path.append((current.x, current.y))
            c = self.came_from[current]
            assert c is not None
            current = c
        return path

    @staticmethod
    def heuristic(a: GridPoint, b: GridPoint) -> int:
        return abs(a.x - b.x) + abs(a.y - b.y)

    def neighbors(self, p: GridPoint) -> Iterable[GridPoint]:
        for d, v in VECTORS.items():
            x = p.x + v[0]
            y = p.y + v[1]
            if (d + 2) % 4 == p.dir:
                # Can't turn around
                continue
            neighbour = GridPoint(x, y, d, 1)
            if not neighbour.in_bounds(self.width, self.height):
                continue
            if d == p.dir:
                if p.speed >= self.maxspeed:
                    continue
                neighbour.speed = p.speed + 1
            elif self.minspeed and p.speed < self.minspeed and (p.x, p.y) != (0, 0):
                continue
            yield neighbour

    def cost(self, a: GridPoint, b: GridPoint) -> int:
        return self.grid[b.y][b.x]

    def a_star_search(self, start: GridPoint, goal: GridPoint) -> GridPoint:
        openset = PriorityQueue[GridPoint]()
        openset.put(start, 0)
        self.came_from: dict[GridPoint, Optional[GridPoint]] = {}
        self.cost_so_far: dict[GridPoint, int] = {}
        self.came_from[start] = None
        self.cost_so_far[start] = 0

        while not openset.empty():
            current: GridPoint = openset.get()
            if (
                current.x == goal.x
                and current.y == goal.y
                and current.speed >= self.minspeed
            ):
                return current

            for next in self.neighbors(current):
                new_cost = self.cost_so_far[current] + self.cost(current, next)
                if next not in self.cost_so_far or new_cost < self.cost_so_far[next]:
                    self.cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(next, goal)
                    openset.put(next, priority)
                    self.came_from[next] = current
        raise Exception("Not possible")


class Day17:
    def __init__(self, input_filename: str = "day17.txt") -> None:
        self.parse_data(self.read_file(input_filename))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(os.path.join("inputs", filename), "r") as file:
            return file.read()

    def parse_data(self, data: str) -> None:
        self.grid = Grid(data.rstrip().split("\n"))

    def part1(self) -> int:
        start = GridPoint(0, 0, 1, 1)
        end = GridPoint(self.grid.width - 1, self.grid.height - 1, 1, 1)
        end = self.grid.a_star_search(start, end)
        # self.grid.draw_path(start, end)
        return self.grid.cost_so_far[end]

    def part2(self) -> int:
        start = GridPoint(0, 0, 1, 0)
        end = GridPoint(self.grid.width - 1, self.grid.height - 1, 1, 1)
        self.grid.minspeed = 4
        self.grid.maxspeed = 10
        end = self.grid.a_star_search(start, end)
        # self.grid.draw_path(start, end)
        return self.grid.cost_so_far[end]


if __name__ == "__main__":
    day = Day17()
    print(day.part1())
    print(day.part2())
