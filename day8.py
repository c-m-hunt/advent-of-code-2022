from typing import List
import numpy as np
import utils

DAY = 8


def load_and_parse_data(day: int, test: bool = False) -> np.array:
    data = utils.get_input(day, test)
    return np.array([[int(i) for i in line] for line in data])


def solve_part_1(data):
    count = 0
    height, width = data.shape
    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                count += 1
            else:
                tree = data[i][j]
                if (np.amax(data[i, 0:j]) < tree or
                        np.amax(data[i, j + 1:width]) < tree or
                        np.amax(data[0:i, j]) < tree or
                        np.amax(data[i + 1:height, j]) < tree):
                    count += 1

    return count


def solve_part_2(data):
    scenic = []
    height, width = data.shape
    for i in range(height):
        for j in range(width):
            tree = data[i][j]
            ranges = [
                np.flip(data[i, 0:j]),
                data[i, j + 1:width],
                np.flip(data[0:i, j]),
                data[i + 1:height, j]
            ]
            tree_scenic = []
            for r in ranges:
                count = 0
                for v in r:
                    count += 1
                    if v >= tree:
                        break
                tree_scenic.append(count)
            scenic.append(np.prod(tree_scenic))
    return max(scenic)


if __name__ == "__main__":
    data = load_and_parse_data(DAY)
    print("Part 1:", solve_part_1(data))
    print("Part 2:", solve_part_2(data))
