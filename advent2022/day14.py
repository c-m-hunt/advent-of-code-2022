from typing import List
import numpy as np
from advent2022 import utils

OFFSET = 10000


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    data = [
        r.split("->")
        for r in data]
    data = [
        [(int(d.split(",")[1]), int(d.split(",")[0])) for d in r]
        for r in data]
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
                if c[0] > c1[0]:
                    c, c1 = c1, c
                if c[1] > c1[1]:
                    c, c1 = c1, c
                grid[c[0]: c1[0] + 1,
                     c[1]: c1[1] + 1] = 1
    return grid, min_x, min_y, max_x, max_y


def print_map(map, min_x, min_y, max_x, max_y):
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            print(int(map[i, j]), end="")
        print()
    print("---")
    # print(min_x, max_x, min_y, max_y)
    # print(map[min_x:max_x + 1, min_y:max_y + 1])


def drop_grain(grid, max_row):
    col, row = OFFSET + 500, 0
    settled = False
    while row < max_row and grid[row, col] == 0:
        if grid[row + 1, col] == 0:
            row += 1
            continue
        if grid[row + 1, col] >= 1:
            if grid[row + 1, col - 1] == 0:
                col -= 1
                row += 1
                continue
            if grid[row + 1, col + 1] == 0:
                col += 1
                row += 1
                continue
            grid[row, col] = 2
            settled = True
            break
    return grid, settled


def drop_sand(grid, max_row):
    settled = True
    count_grains = 0
    while True:
        grid, settled = drop_grain(grid, max_row)
        if not settled:
            break
        count_grains += 1
    return count_grains, grid


def solve_part_1(data):
    data = [
        [
            (l[0], l[1] + OFFSET) for l in ls
        ]
        for ls in data
    ]
    map, min_x, min_y, max_x, max_y = draw_map(data)
    grains, grid = drop_sand(map, max_x)
    return grains


def solve_part_2(data):
    data = [
        [
            (l[0], l[1] + OFFSET) for l in ls
        ]
        for ls in data
    ]
    min_x, min_y, max_x, max_y = get_max_and_min(data)
    data.append([(max_x + 2, 0), (max_x + 2, max_y + OFFSET)])
    map, min_x, min_y, max_x, max_y = draw_map(data)
    grains, grid = drop_sand(map, max_x)
    return grains
