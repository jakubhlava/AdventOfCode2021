with open("input.txt", "r") as f:
    positions = [int(x) for x in f.read().strip().split(",")]

minpos, maxpos = min(positions), max(positions)
minfuel, minfuel2 = None, None

for i in range(minpos, maxpos):
    fuel = sum([abs(x-i) for x in positions])
    fuel2 = sum([int(abs(x-i)*((1+abs(x-i))/2)) for x in positions])
    if not minfuel or fuel < minfuel:
        minfuel = fuel
    if not minfuel2 or fuel2 < minfuel2:
        minfuel2 = fuel2

print("Part 1:", minfuel)
print("Part 2:", minfuel2)