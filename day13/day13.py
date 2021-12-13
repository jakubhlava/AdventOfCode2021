import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()
points, commands = [], []
for ln in lines:  # parse vstupu
    if "," in ln:
        points.append(tuple([int(x) for x in ln.split(",")][::-1]))  # ::-1 protože numpy vs. zadání AoC
    elif ln != "\n":
        commands.append(ln.strip().split(" ")[-1].split("="))
maxx = max([x[0] for x in points])+1
maxy = max([y[1] for y in points])+1
mat = np.zeros((maxx, maxy), dtype=np.int16)
for p in points:
    mat[p] = 1
for i, c in enumerate(commands):
    amount = int(c[1])
    if c[0] == "y":
        mat1 = mat[:amount, :]    # rozpulení matice
        mat2 = mat[amount+1:, :]
        mat2 = np.flip(mat2, 0)   # překlopení
        mat = mat1+mat2           # přiložení na sebe
    elif c[0] == "x":
        mat1 = mat[:, :amount]
        mat2 = mat[:, amount+1:]
        mat2 = np.flip(mat2, 1)
        mat = mat1+mat2
    if i == 0: # part 1 po prvním běhu
        mat[mat > 1] = 1
        print("Part 1:", np.sum(mat))
print("Part 2:")
for line in mat:
    print(''.join(["#" if x >= 1 else " " for x in line]))