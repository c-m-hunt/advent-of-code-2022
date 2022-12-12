from typing import List, Tuple, Optional
import numpy as np

from advent2022 import utils
import sys
sys.setrecursionlimit(5000)


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return np.array([[*s] for s in data])


char_map = {
    c: i
    for i, c in enumerate(
        "SabcdefghijklmnopqrstuvwxyzE"
    )
}


def get_start_and_end_points(grid):
    global char_map
    start = None
    target = None
    max_value = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if char_map.get(grid[i, j], 0) > max_value:
                max_value = char_map[grid[i, j]]
            if grid[i, j] == 'S':
                start = (i, j)
            if grid[i, j] == 'E':
                target = (i, j)
    return start, target


move = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1),
}

points_visited = None
route = []


def valid_move(grid, from_point, to_point):
    try:
        from_point_value = char_map.get(
            grid[from_point[0], from_point[1]], None)
        to_point_value = char_map.get(grid[to_point[0], to_point[1]], None)
        if grid[to_point[0], to_point[1]] in ["S", "E"]:
            return True
        if from_point_value - to_point_value <= 1:
            return True
        return False
    except Exception:
        return False


routes = []


def get_directions(grid, point):
    directions = {
        "up": grid[point[0] - 1, point[1]] if point[0] - 1 >= 0 else None,
        "down": grid[point[0] + 1, point[1]] if point[0] + 1 < grid.shape[0] else None,
        "left": grid[point[0], point[1] - 1] if point[1] - 1 >= 0 else None,
        "right": grid[point[0], point[1] + 1] if point[1] + 1 < grid.shape[1] else None,
    }

    dir_vals = {
        "up": char_map.get(directions["up"], None),
        "down": char_map.get(directions["down"], None),
        "left": char_map.get(directions["left"], None),
        "right": char_map.get(directions["right"], None),
    }

    sorted_directions = dict(sorted(
        dir_vals.items(), key=lambda x: x[1] if x[1] else 0))
    return sorted_directions.keys()


def solve_map(grid, start, target):
    global step_count
    if start == target:
        routes.append(route.copy())
        print(len(route))
        return False

    for direction in get_directions(grid, target):
        new_point = move[direction](target)
        if (
            new_point[0] >= 0 and
            new_point[1] >= 0 and
            valid_move(grid, target, new_point) and
            points_visited[new_point[0], new_point[1]] == 0
        ):
            route.append(new_point)
            points_visited[new_point[0], new_point[1]] = 1
            if solve_map(grid, start, new_point):
                return True
            points_visited[new_point[0], new_point[1]] = 0
    return False


def solve_part_1(data):
    start, end = get_start_and_end_points(data)
    print(start, end)
    global points_visited
    points_visited = np.zeros(data.shape)
    try:
        resolved = solve_map(data, start, end)
        print(resolved)
        print(route)
        print("Length", len(routes))
        print(min([len(r) for r in routes]))
    except Exception as e:
        print(e)
    return min([len(r) for r in routes])


def solve_part_2(data):
    pass
