import numpy as np
from itertools import cycle

def make_position(line):
    start, stop = line.split(" -> ")
    sx, sy = start.split(",")
    stx, sty = stop.split(",")
    return {
        "start": (int(sx), int(sy)),
        "stop": (int(stx), int(sty))
    }

with open("input.txt", "r") as f:
    vents = [make_position(line) for line in f.readlines()]

x = [v['start'][0] for v in vents]
x.extend([v['stop'][0] for v in vents])
y = [v['start'][1] for v in vents]
y.extend([v['stop'][1] for v in vents])
matrix_size = (max(x)+1, max(y)+1)
matrix, matrix2 = np.zeros(matrix_size, dtype=np.int32), np.zeros(matrix_size, dtype=np.int32)

for vent in vents:
    positions = {vent["start"], vent["stop"]}
    if vent["start"][0] < vent["stop"][0]:
        xdir = 1
    elif vent["start"][0] == vent["stop"][0]:
        xdir = 0
    else:
        xdir = -1
    if vent["start"][1] < vent["stop"][1]:
        ydir = 1
    elif vent["start"][1] == vent["stop"][1]:
        ydir = 0
    else:
        ydir = -1
    x = range(vent["start"][0], vent["stop"][0], xdir) if xdir != 0 else cycle([vent["start"][0]])
    y = range(vent["start"][1], vent["stop"][1], ydir) if ydir != 0 else cycle([vent["start"][1]])
    for p in zip(x,y):
        positions.add(p)
    for p in positions:
        if xdir == 0 or ydir == 0:
            matrix[p] += 1
        matrix2[p] += 1

overlaps = matrix[matrix > 1]
overlaps2 = matrix2[matrix2 > 1]
print(f"Part 1: {len(overlaps)}")
print(f"Part 2: {len(overlaps2)}")