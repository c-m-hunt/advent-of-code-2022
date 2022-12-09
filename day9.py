from typing import List
import numpy as np

import utils

DAY = 9


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return [l.split(" ") for l in data]


def solve_part_1(data):
    visited = np.zeros((1000, 1000))
    H, T = [4, 0], [4, 0]
    visited[T[0], T[1]] = 1
    for l in data:
        direction, distance = l[0], int(l[1])
        print(direction, distance)
        if direction == "U":
            idx, step = 0, -1
        elif direction == "D":
            idx, step = 0, 1
        elif direction == "L":
            idx, step = 1, -1
        elif direction == "R":
            idx, step = 1, 1

        for i in range(distance):
            H[idx] += step
            if abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
                for move_idx in range(2):
                    if H[move_idx] == T[move_idx]:
                        continue
                    move = 1 if H[move_idx] > T[move_idx] else -1
                    T[move_idx] += move
            print("H:", H, "T:", T)
            visited[T[0], T[1]] = 1

    print(visited)
    # return 3
    return np.sum(visited)


def solve_part_2(data):
    pass


if __name__ == "__main__":
    data = load_and_parse_data(DAY)
    print(data)
    print("Part 1:", solve_part_1(data))
    print("Part 2:", solve_part_2(data))
