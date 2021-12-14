from math import ceil
with open("input.txt", "r") as f:
    lines = f.readlines()

polymer = lines[0].strip()  # základní polymer
# příkazy pro vkládání, překládají původní pár -> dva nové páry vzniklé vložením
commands = {x[0]: (x[0][0]+x[1], x[1]+x[0][1]) for x in [y.strip().split(" -> ") for y in lines[2:]]}
# vyhledání všech možných písmen kvůli kvantitám (vkládání může přidávat písmena, která v polymeru nebyla)
allletters = set()
for l in ''.join(commands.keys()):
    allletters.add(l)
# počítadlo párů + naplnění ze základního polymeru
pairs = {c: 0 for c in commands.keys()}
for i in range(len(polymer)-1):
    pairs[polymer[i:i+2]] += 1
# rozvoj polymeru
for step in range(40):
    newpairs = {p: 0 for p in pairs.keys()}  # nový dict, protože potřebujeme kroky oddělit bez prolínání
    for k in pairs.keys():                   # na všechny staré páry aplikujeme pravidlo a vytvoříme dva nové páry
        newkeys = commands[k]
        newpairs[newkeys[0]] += pairs[k]
        newpairs[newkeys[1]] += pairs[k]
    pairs = newpairs
    if step == 9 or step == 39:             # při 10. a 40. kroku sečteme a vypíšeme
        quantities = {letter: 0 for letter in allletters}
        for k in pairs.keys():  # protože ukládáme počty PÁRŮ, tak jsou téměř všechna písmena započtena 2x
            quantities[k[0]] += pairs[k] / 2
            quantities[k[1]] += pairs[k] / 2
        # první a poslední písmena jsou započtena pouze 1x, proto byla "rozpůlena" při součtu, zaokrouhlíme nahoru...
        for k in quantities.keys():
            quantities[k] = int(ceil(quantities[k]))
        if step == 9:
            print("Part 1:", end=" ")
        else:
            print("Part 2:", end=" ")
        print(max(quantities.values())-min(quantities.values()))

