from typing import List, Tuple, Optional
import numpy as np

from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return np.array([[*s] for s in data])


char_map = {
    c: i
    for i, c in enumerate(
        "abcdefghijklmnopqrstuvwxyz"
    )
}


def get_start_and_end_points(grid):
    start = None
    target = None
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 'S':
                start = (i, j)
            if grid[i, j] == 'E':
                target = (i, j)
    return start, target


def get_directions(grid, point):
    directions = {
        "up": grid[point[0] - 1, point[1]] if point[0] - 1 >= 0 else None,
        "down": grid[point[0] + 1, point[1]] if point[0] + 1 < grid.shape[0] else None,
        "left": grid[point[0], point[1] - 1] if point[1] - 1 >= 0 else None,
        "right": grid[point[0], point[1] + 1] if point[1] + 1 < grid.shape[1] else None,
    }

    return {
        "up": char_map.get(directions["up"], -1 if directions["up"] == "S" else None),
        "down": char_map.get(directions["down"], -1 if directions["down"] == "S" else None),
        "left": char_map.get(directions["left"], -1 if directions["left"] == "S" else None),
        "right": char_map.get(directions["right"], -1 if directions["right"] == "S" else None),
    }


move = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1),
}


def get_available_points(grid, point) -> Optional[Tuple[int, int]]:
    directions = get_directions(grid, point)
    curr_value = char_map.get(grid[point[0], point[1]], None)
    sort_dir = True if curr_value is None else False
    sorted_directions = dict(sorted(
        directions.items(), key=lambda x: x[1] if x[1] else 0, reverse=sort_dir))

    available_points = []
    for direction, value in sorted_directions.items():
        if value is not None and (
            curr_value is None or value == -
                1 or (value == curr_value - 1) or value >= curr_value
        ):
            available_points.append(move[direction]((point[0], point[1])))
            if curr_value is None:
                break
    return available_points


step_count = 0
points_visited = None
route = []


def solve_map(grid, start, target):
    global step_count
    if start == target:
        return True

    step_count += 1
    available_points = get_available_points(grid, target)
    for point in available_points:
        route.append(point)
        if points_visited[point[0], point[1]] == 1:
            continue
        points_visited[point[0], point[1]] = 1
        if solve_map(grid, start, point):
            return True
        points_visited[point[0], point[1]] = 0
        step_count -= 1
        route.pop()
        print(route)
        return False
    return False


def solve_part_1(data):
    start, end = get_start_and_end_points(data)
    print(start, end)
    global points_visited
    points_visited = np.zeros(data.shape)
    resolved = solve_map(data, start, end)
    print(resolved)
    print(route)
    return step_count


def solve_part_2(data):
    pass
