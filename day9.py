from typing import List
import numpy as np

import utils

DAY = 9


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return [l.split(" ") for l in data]


def new_pos(h, t):
    if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        for move_idx in range(2):
            if h[move_idx] == t[move_idx]:
                continue
            move = 1 if h[move_idx] > t[move_idx] else -1
            t[move_idx] += move
    return t


def solve_rope(data, tail_length):
    visited = np.zeros((10000, 10000))
    h, tail = [4, 0], [[4, 0] for l in range(tail_length)]
    visited[tail[0][0], tail[0][1]] = 1
    for l in data:
        direction, distance = l[0], int(l[1])
        if direction == "U":
            idx, step = 0, -1
        elif direction == "D":
            idx, step = 0, 1
        elif direction == "L":
            idx, step = 1, -1
        elif direction == "R":
            idx, step = 1, 1

        for i in range(distance):
            h[idx] += step
            for j, _ in enumerate(tail):
                follow = tail[j - 1] if j > 0 else h
                tail[j] = new_pos(follow, tail[j])
                if j == tail_length - 1:
                    visited[tail[j][0], tail[j][1]] = 1

    return np.sum(visited)


def solve_part_1(data):
    return solve_rope(data, 1)


def solve_part_2(data):
    return solve_rope(data, 9)


if __name__ == "__main__":
    data = load_and_parse_data(DAY)
    print("Part 1:", solve_part_1(data))
    print("Part 2:", solve_part_2(data))
