from typing import List

from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    pairs = []
    pair = None
    for line in data:
        if line.strip() == '':
            continue
        if not pair:
            pair = [eval(line)]
        else:
            pair.append(eval(line))
            pairs.append(pair)
            pair = None
    return pairs


def compare_pair(left, right):
    left_type = "int" if isinstance(left, int) else "list"
    right_type = "int" if isinstance(right, int) else "list"

    if left_type == "int" and right_type == "int":
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None

    if left_type == "int" and right_type == "list":
        left = [left]

    if left_type == "list" and right_type == "int":
        right = [right]

    index = 0
    while True:
        l = left[index] if index < len(left) else None
        r = right[index] if index < len(right) else None
        if l is None and r is None:
            return True
        if l is None:
            return True
        if r is None:
            return False
        compare = compare_pair(l, r)
        if compare is None:
            index += 1
            continue
        return compare


def solve(pairs):
    correct_count = 0
    pair_index = 1
    for pair in pairs:
        left, right = pair
        correct = compare_pair(left, right)
        print(left, right, correct, pair_index)
        correct_count += pair_index if correct else 0
        pair_index += 1

    return correct_count


def solve_part_1(data):
    # 6695 too high
    return solve(data)


def solve_part_2(data):
    pass
