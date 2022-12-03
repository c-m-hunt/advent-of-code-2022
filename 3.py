filename = "./input/3.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

priorities = {l: i + 1 for i, l in enumerate(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

total = 0
for bp in lines:
    bp1 = bp[:len(bp) // 2]
    bp2 = bp[len(bp) // 2:]

    intersect = set(bp1).intersection(set(bp2))
    total += priorities[list(intersect)[0]]

print("Part 1:", total)

i = 0
total = 0
while i < len(lines):
    intersect1 = set(lines[i]).intersection(set(lines[i + 1]))
    intersect2 = intersect1.intersection(set(lines[i + 2]))
    total += priorities[list(intersect2)[0]]
    i += 3

print("Part 2:", total)
