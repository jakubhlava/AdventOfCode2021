with open("input.txt", "r") as f:
    cases = [x.strip().split(" | ") for x in f.readlines()]

easynums = 0
for case in cases:
    easynums += len([len(x) for x in case[1].split() if len(x) in [2, 3, 4, 7]])
print(f"Part 1: {easynums}")

p2sum = 0
for case in cases:
    observed = case[0].split()
    mapping = {}
    reverse_map = {}
    segment = {}
    sorted_by_segments = {x: [] for x in range(2, 8)}
    for num in observed:
        sorted_by_segments[len(num)].append(set(num))
    mapping[''.join(sorted(sorted_by_segments[2][0]))] = "1"
    reverse_map[1] = set(sorted_by_segments[2][0])
    mapping[''.join(sorted(sorted_by_segments[3][0]))] = "7"
    reverse_map[7] = set(sorted_by_segments[3][0])
    mapping[''.join(sorted(sorted_by_segments[4][0]))] = "4"
    reverse_map[4] = set(sorted_by_segments[4][0])
    mapping[''.join(sorted(sorted_by_segments[7][0]))] = "8"
    reverse_map[8] = set(sorted_by_segments[7][0])
    segment["a"] = reverse_map[7] - reverse_map[1]
    for seg in sorted_by_segments[5]:
        if reverse_map[7].issubset(seg):
            mapping[''.join(sorted(seg))] = "3"
            reverse_map[3] = seg
            segment["g"] = reverse_map[3] - reverse_map[7] - reverse_map[4]
            segment["d"] = reverse_map[3] - reverse_map[7] - segment["g"]
            break
    sorted_by_segments[5].remove(reverse_map[3])
    zero = reverse_map[8] - segment["d"]
    reverse_map[0] = zero
    mapping[''.join(sorted(zero))] = "0"
    sorted_by_segments[6].remove(zero)
    for seg in sorted_by_segments[6]:
        if reverse_map[4].issubset(seg):
            mapping[''.join(sorted(seg))] = "9"
            reverse_map[9] = seg
            segment["e"] = reverse_map[8] - reverse_map[9]
            break
    sorted_by_segments[6].remove(reverse_map[9])
    for seg in sorted_by_segments[5]:
        if seg.issubset(reverse_map[8]) and not segment["e"].issubset(seg):
            mapping[''.join(sorted(seg))] = "5"
            reverse_map[5] = seg
            break
    sorted_by_segments[5].remove(reverse_map[5])
    mapping[''.join(sorted(sorted_by_segments[5][0]))] = "2"
    reverse_map[2] = sorted_by_segments[5][0]
    mapping[''.join(sorted(sorted_by_segments[6][0]))] = "6"
    reverse_map[6] = sorted_by_segments[6][0]
    p2sum += int(''.join([mapping[''.join(sorted(x))] for x in case[1].split()]))

print("Part 2:", p2sum)