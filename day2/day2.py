with open("input.txt", "r") as f:
    commands = [x.split(" ") for x in f.readlines()]

depth = 0
depth2 = 0
position = 0
aim = 0
for c in commands:
    match c[0]:
        case "forward":
            position += int(c[1])
            depth2 += int(c[1])*aim
        case "down":
            depth += int(c[1])
            aim += int(c[1])
        case "up":
            depth -= int(c[1])
            aim -= int(c[1])

print(f"Result part 1: {depth*position}")
print(f"Result part 2: {depth2*position}")
