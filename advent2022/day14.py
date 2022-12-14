from typing import List
import numpy as np
from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    data = [
        r.split("->")
        for r in data]
    data = [
        [(int(d.split(",")[1]), int(d.split(",")[0])) for d in r]
        for r in data]
    print(data)
    return data


def get_max_and_min(data):
    xs = [
        p[0] for d in data
        for p in d
    ]
    min_x, max_x = min(xs), max(xs)
    ys = [
        p[1] for d in data
        for p in d
    ]
    min_y, max_y = min(ys), max(ys)
    return min_x, min_y, max_x, max_y


def draw_map(data):
    min_x, min_y, max_x, max_y = get_max_and_min(data)
    grid = np.zeros((max_x + 1, max_y + 1))
    for d in data:
        for i, c in enumerate(d):
            if i < len(d) - 1:
                c1 = d[i+1]
                print(c, c1)
                if c[0] > c1[0]:
                    c, c1 = c1, c
                if c[1] > c1[1]:
                    c, c1 = c1, c
                grid[c[0]: c1[0] + 1,
                     c[1]: c1[1] + 1] = 1
                print_map(grid, min_x, min_y, max_x, max_y)

    return grid, min_x, min_y, max_x, max_y


def print_map(map, min_x, min_y, max_x, max_y):
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            print(int(map[i, j]), end="")
        print()
    print("---")
    # print(min_x, max_x, min_y, max_y)
    # print(map[min_x:max_x + 1, min_y:max_y + 1])


def solve_part_1(data):
    map, min_x, min_y, max_x, max_y = draw_map(data)
    print_map(map, min_x, min_y, max_x, max_y)


def solve_part_2(data):
    pass
