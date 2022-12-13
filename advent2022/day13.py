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
    l_len, r_len = len(left), len(right)

    for i in range(l_len):
        l = left[i]
        r = right[index] if index < len(right) else None
        if r is None:
            return False
        compare = compare_pair(l, r)
        if compare is None:
            index += 1
            continue
        return compare
    if l_len < r_len:
        return True
    return None


def solve(pairs):
    correct_count = 0
    pair_index = 1
    for pair in pairs:
        left, right = pair
        correct = compare_pair(left, right)
        correct_count += pair_index if correct else 0
        pair_index += 1

    return correct_count


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def sort(packets):
    swaps = 0
    while True:
        swaps = 0
        for j in range(len(packets) - 1):
            comp = compare_pair(packets[j], packets[j + 1])
            if comp is False:
                swaps += 1
                packets = swapPositions(packets, j, j + 1)
        if swaps == 0:
            break
    return packets


def solve_part_1(data):
    return solve(data)


def solve_part_2(data):
    dividers = [[2]], [[6]]
    packets = [*dividers]
    for packet in data:
        packets.extend(packet)
    packets = sort(packets)
    divider_idxs = [i+1 for i,
                    packet in enumerate(packets) if packet in dividers]
    return divider_idxs[0] * divider_idxs[1]
