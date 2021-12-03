from collections import Counter
with open("input.txt", "r") as f:
    numbers = [line.strip() for line in f.readlines()]

columns = [[] for _ in range(len(numbers[0]))]
for num in numbers:
    for index, n in enumerate(num):
        columns[index].append(n)

result = []
for col in columns:
    result.append(Counter(col).most_common(1)[0][0])

gamma = int(''.join(result), 2)
epsilon = int(''.join(['0' if x == '1' else '1' for x in result]), 2)
print(f"Part 1: {gamma*epsilon}")

oxy = [n for n in numbers]
co2 = [n for n in numbers]
cursor = 0
while len(oxy) > 1:
    mc = Counter(sorted([x[cursor] for x in oxy], reverse=True)).most_common(1)[0][0]
    oxy = [n for n in oxy if n[cursor] == mc]
    cursor += 1

cursor = 0
while len(co2) > 1:
    lc = Counter(sorted([x[cursor] for x in co2], reverse=True)).most_common()[-1][0]
    co2 = [n for n in co2 if n[cursor] == lc]
    cursor += 1

print(f"Part 2: {int(''.join(oxy), 2)*int(''.join(co2), 2)}")