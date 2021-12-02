with open("input.txt", "r") as f:
    numbers = [int(x) for x in f.readlines()]

# Part 1
last = None
inc = 0
for num in numbers:
    if last:
        if num > last:
            inc += 1
    last = num

print(f"Increasing: {inc}")

# Part 2
sums = []
for i in range(len(numbers)-2):
    sums.append(sum([numbers[i], numbers[i+1], numbers[i+2]]))

last = None
inc = 0
for num in sums:
    if last:
        if num > last:
            inc += 1
    last = num

print(f"Increasing: {inc}")
