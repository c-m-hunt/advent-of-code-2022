from typing import List, Tuple

import utils

import utils


def load_and_parse_data(day: int, test: bool = False) -> (Tuple[List[List[str]]], Tuple[int, int, int]):
    data = utils.get_input(day, test)
    instructions = []
    cols = []

    for i, l in enumerate(data):
        if "[" not in l:
            cols = data[i].split()
            cols = [int(c) for c in cols]
            break
    stack_count = max(cols)
    stacks = [[] for _ in range(stack_count)]
    for l in data:
        if "[" in l:
            for col in cols:
                which = 1 + ((col - 1) * 4)
                if which > len(l):
                    break
                if l[which] == " ":
                    continue
                stacks[col-1].append(l[which])
            continue
        if l.startswith("move"):
            l = l.replace("move", "").strip()
            i1 = l.split("from")[0].strip()
            i2 = l.split("from")[1].split("to")[0].strip()
            i3 = l.split("from")[1].split("to")[1].strip()
            move = tuple([int(i1), int(i2), int(i3)])
            instructions.append(move)
    for s in stacks:
        s.reverse()
    return stacks, instructions


def solve_part_1(data: Tuple[any, any]) -> str:
    stacks, instructions = data
    for inst in instructions:
        for i in range(inst[0]):
            stacks[inst[2]-1].append(stacks[inst[1]-1].pop())
    return "".join([s[-1]
                    for s in stacks])


def solve_part_2(data: Tuple[any, any]) -> str:
    stacks, instructions = data
    for inst in instructions:
        to_move = stacks[inst[1]-1][len(stacks[inst[1]-1]) - (inst[0]):]
        stacks[inst[1]-1] = stacks[inst[1] -
                                   1][:len(stacks[inst[1]-1]) - (inst[0])]
        stacks[inst[2]-1] = stacks[inst[2]-1] + to_move

    return "".join([s[-1]
                    for s in stacks])


if __name__ == "__main__":
    data = load_and_parse_data(5)
    print("Part 1:", solve_part_1(data))
    data = load_and_parse_data(5)
    print("Part 2:", solve_part_2(data))
