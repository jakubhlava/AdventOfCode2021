with open("input.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]

points = {")": 3, "]": 57, "}": 1197, ">": 25137}   # ohodnocení pro part 1
points2 = {"(": 1, "[": 2, "{": 3, "<": 4}          # ohodnocení pro part 2
end_to_open = {")": "(", "]": "[", "}": "{", ">": "<"}  # abych si ušetřil složitý if:elif:else
score = 0   # part 1 score
scores = []     # seznam part 2 score
for l in lines:
    score2 = 0
    canclose = []   # zásobník otevřených závorek (pouze vrchol je možné zavřít)
    corrupt = False     # indikátor corrupt/incomplete
    for ch in l:
        if ch in "([{<":
            canclose.append(ch)     # pushnu začátek chunku na zásobník
        elif ch in ")]}>":
            if end_to_open[ch] == canclose[-1]:      # pokud je odpovídající závorka vrcholem zásobníku, můžu uzavřit
                canclose.pop()
            else:
                score += points[ch]     # jinak je řádek corrupted
                corrupt = True
                break
    if not corrupt:     # pokud není corrupted, je jistě incomplete
        while len(canclose) > 0:
            # pro všechny zbylé závorky na zásobníku v jejich pořadí na zásobníku vypočítám score
            score2 *= 5
            closing = canclose.pop()
            score2 += points2[closing]
        scores.append(score2)

print("Part 1:", score)
print("Part 2:", sorted(scores)[len(scores)//2]) # získám střední skóre podle zadání
