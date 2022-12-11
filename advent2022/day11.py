from math import floor
import numpy as np
from typing import List, Callable
from dataclasses import dataclass, field
from advent2022 import utils


@dataclass
class Monkey:
    name: str
    index: int
    items: List[int] = field(default_factory=lambda: [])
    operation: Callable = None
    test: Callable = None
    divisor: int = None
    if_true: int = None
    if_false: int = None
    inspections: int = 0


def get_operation(sign, amount) -> Callable:
    if sign == "+":
        return lambda x: x + \
            (int(amount) if amount != "old" else x)
    elif sign == "-":
        return lambda x: x - \
            (int(amount) if amount != "old" else x)
    elif sign == "*":
        return lambda x: x * \
            (int(amount) if amount != "old" else x)
    elif sign == "/":
        return lambda x: x / \
            (int(amount) if amount != "old" else x)


def get_test(div) -> Callable:
    return lambda x: x % div == 0


def load_and_parse_data(day: int, test: bool = False):
    data = utils.get_input(day, test)
    monkeys = []
    for line in data:
        line = line.strip()
        if line.startswith("Monkey"):
            name = line.replace(":", "")
            index = int(line.split(" ")[1].replace(":", ""))
            monkey = Monkey(name, index)
        if line.startswith("Starting items"):
            monkey.items = [int(i.strip())
                            for i in line.split(":")[-1].split(",")]
        if line.startswith("Operation"):
            sign = line.split(" ")[-2]
            amount = line.split(" ")[-1]
            monkey.operation = get_operation(sign, amount)

        if line.startswith("Test"):
            div = int(line.split(" ")[-1])
            monkey.divisor = div
            monkey.test = get_test(div)

        if line.startswith("If true"):
            monkey.if_true = int(line.split(" ")[-1])

        if line.startswith("If false"):
            monkey.if_false = int(line.split(" ")[-1])

        if line == "":
            monkeys.append(monkey)
    monkeys.append(monkey)
    return monkeys


def single_round(monkeys, modulo, worry_divider=None):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspections += 1
            item = item % modulo
            item = monkey.operation(item)
            if worry_divider is not None:
                item = item // worry_divider
            if monkey.test is not None:
                if monkey.test(item):
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)
        monkey.items = []

    return monkeys


def solve(monkeys, rounds, worry_divider):
    modulo = np.product(
        [m.divisor for m in monkeys if m.divisor is not None])

    for _ in range(rounds):
        monkeys = single_round(monkeys, modulo, worry_divider)

    inspections = [m.inspections for m in monkeys]
    inspections.sort()

    return inspections[-2] * inspections[-1]


def solve_part_1(monkeys):
    return solve(monkeys, 20, 3)


def solve_part_2(monkeys):
    return solve(monkeys, 10000, None)
