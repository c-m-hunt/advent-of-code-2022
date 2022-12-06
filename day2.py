

filename = "./input/2.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip().split((" ")) for line in lines]

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


points = []
for game in lines:
    game_points = 0
    if game[1] == lose[game[0]]:
        game_points += 6
    elif game[1] == draw[game[0]]:
        game_points += 3
    game_points += pts[game[1]]
    points.append(game_points)

print("Part 1:", sum(points))

points = []
for game in lines:

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

print("Part 2:", sum(points))
