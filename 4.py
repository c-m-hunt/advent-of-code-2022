from typing import List


def get_range(ranges: List[str]) -> List[int]:
    start = int(ranges.split("-")[0])
    end = int(ranges.split("-")[1])
    return list(range(start, end + 1))


filename = "./input/4.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip().split(",") for line in lines]

full_intersect = 0
for p in lines:
    e1 = get_range(p[0])
    e2 = get_range(p[1])
    if len(set(e1).intersection(set(e2))) == len(set(e1)) or len(set(e2).intersection(set(e1))) == len(set(e2)):
        full_intersect += 1

print("Part 1:", full_intersect)

part_intersect = 0
for p in lines:
    e1 = get_range(p[0])
    e2 = get_range(p[1])
    if len(set(e1).intersection(set(e2))) > 0:
        part_intersect += 1

print("Part 2:", part_intersect)
