with open("input.txt", "r") as f:
    lanternfish = [int(x) for x in f.read().strip().split(",")]

counts = {i: lanternfish.count(i) for i in range(9)}
for i in range(256):
    for j in range(0, 9):
        counts[j-1] = counts[j]
    counts[8] = counts[-1]
    counts[6] += counts[8]
    if i == 79:
        print("Part 1:", sum([counts[x] for x in range(0, 9)]))
print("Part 2:", sum([counts[x] for x in range(0, )]))
