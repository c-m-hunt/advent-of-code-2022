from typing import List

import utils

DAY = 7


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    return utils.get_input(day, test)


def solve_part_1(data: List[str]) -> int:
    dir_size = get_dir_sizes(data)
    return sum([s for s in dir_size.values() if s < 100000])


def solve_part_2(data):
    dir_size, max_size, req_size = get_dir_sizes(data), 70000000, 30000000
    intial_size = dir_size["/"]
    curr_closest = None
    curr_closest_size = None
    for key, size in dir_size.items():
        pot_remaining_size = max_size - (intial_size - size)
        if pot_remaining_size < req_size:
            print(key, size, pot_remaining_size, "Continue")
            continue
        if curr_closest is None or pot_remaining_size < curr_closest:
            curr_closest, curr_closest_size = pot_remaining_size, size
    return curr_closest_size


def get_dir_sizes(data):
    curr_dir, dir_size = [], {}
    for line in data:
        if line.startswith("$ cd"):
            directory = line.split(" ")[-1]
            curr_dir.pop() if directory == ".." else curr_dir.append(directory)
            continue
        if line.startswith("$ ls") or line.startswith("dir"):
            continue
        size = int(line.split(" ")[0])
        for i in range(len(curr_dir)):
            key = "/".join(curr_dir[:i + 1])
            dir_size[key] = dir_size.get(key, 0) + size
    return dir_size


if __name__ == "__main__":
    data = load_and_parse_data(DAY)
    print("Part 1:", solve_part_1(data))
    print("Part 2:", solve_part_2(data))
