from typing import List

from advent2022 import utils


def load_and_parse_data(day: int, test: bool = False) -> List[str]:
    data = utils.get_input(day, test)
    return [line.rstrip().split((" ")) for line in data]


pts = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

draw = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

lose = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}


def solve_part_1(data):
    points = []
    for game in data:
        game_points = 0
        if game[1] == lose[game[0]]:
            game_points += 6
        elif game[1] == draw[game[0]]:
            game_points += 3
        game_points += pts[game[1]]
        points.append(game_points)

    return sum(points)


def solve_part_2(data):
    points = []
    for game in data:

        my_choice = ""
        if game[1] == "X":
            my_choice = win[game[0]]
        elif game[1] == "Y":
            my_choice = draw[game[0]]
        elif game[1] == "Z":
            my_choice = lose[game[0]]

        game_points = 0
        if my_choice == lose[game[0]]:
            game_points += 6
        elif my_choice == draw[game[0]]:
            game_points += 3
        game_points += pts[my_choice]
        points.append(game_points)

    return sum(points)
