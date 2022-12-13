from typing import List
import numpy as np
from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return np.array([[*s] for s in data])


CHAR_MAP = {
    c: i
    for i, c in enumerate(
        "SabcdefghijklmnopqrstuvwxyzE"
    )
}


def get_all_points_of_value(grid, value):
    points = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == value:
                points.append((i, j))
    return points


def get_start_and_end_points(grid):
    start = None
    target = None
    max_value = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if CHAR_MAP.get(grid[i, j], 0) > max_value:
                max_value = CHAR_MAP[grid[i, j]]
            if grid[i, j] == 'S':
                start = (i, j)
            if grid[i, j] == 'E':
                target = (i, j)
    return start, target


def valid_move(grid, from_point, to_point):
    if 0 > to_point[0] or to_point[0] >= grid.shape[0]:
        return False
    from_point_value = CHAR_MAP.get(
        grid[from_point[0], from_point[1]], None)
    to_point_value = CHAR_MAP.get(grid[to_point[0], to_point[1]], None)
    if from_point_value - to_point_value >= -1:
        return True
    return False


def solve_map(grid, start, target):
    calc_grid = np.zeros(grid.shape)
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    moves_to_test, next_moves_to_test, step = [start], [], 0
    while True:
        step += 1
        for m_f in moves_to_test:
            for m_t in moves:
                new_point = (m_f[0] + m_t[0], m_f[1] + m_t[1])
                if (0 > new_point[0] or new_point[0] >= grid.shape[0]
                        or 0 > new_point[1] or new_point[1] >= grid.shape[1]):
                    continue
                if calc_grid[new_point[0], new_point[1]] != 0:
                    continue
                if grid[new_point[0], new_point[1]] == "S":
                    continue
                if valid_move(grid, m_f, new_point):
                    calc_grid[new_point[0], new_point[1]] = step
                    next_moves_to_test.append(new_point)
                    if new_point == target:
                        return calc_grid[target[0], target[1]]
        moves_to_test = next_moves_to_test.copy()
        next_moves_to_test = []
        if len(moves_to_test) == 0:
            return None


def solve_part_1(data):
    start, end = get_start_and_end_points(data)
    resolved = solve_map(data, start, end)
    return resolved


def solve_part_2(data):
    start, end = get_start_and_end_points(data)
    lowest_points = [start]
    lowest_points.extend(get_all_points_of_value(data, 'a'))
    distances = []
    for p in lowest_points:
        distances.append(solve_map(data, p, end))
    return min([d for d in distances if d is not None])
