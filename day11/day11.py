import numpy as np


def neighbors(x, y, matrix):  # získá souřadnice osmiokolí bodu s filtrací bodů mimo pole
    n = []
    for x0 in range(x-1,x+2):
        for y0 in range(y-1,y+2):
            if 0 <= x0 < len(matrix) and 0 <= y0 < len(matrix[0]):
                n.append((x0,y0))
    return n


with open("input.txt", "r") as f:
    levels = [list(x.strip()) for x in f.readlines()]

energy = np.array(levels, dtype=np.int32)
flashes = 0  # počet flashů (part 1)
run = 0  # počet běhů (part 2 synchronizace)
while True:
    energy += 1  # zvýší energii všem
    to_flash = [tuple(x) for x in np.argwhere(energy > 9)] # jako základ vybere souřadnice všech s energií > 9
    flashed = []
    while len(to_flash) > 0:
        pos = to_flash.pop()  # zásobník na chobotnice které teprve mají provést flash
        flashed.append(pos)   # pole pro filtraci vícvenásobných flashnutí + pro reset energie
        neighbor_list = neighbors(*pos, energy)
        for neighbor in neighbor_list:
            energy[neighbor] += 1
            # nutná kontrola, jestli chobotnice už neflashnula, není v čekacím zásobníku a má dostatečnou energii
            if energy[neighbor] > 9 and neighbor not in flashed and neighbor not in to_flash:
                to_flash.append(neighbor)
    for f in flashed:   # vyresetovat energii chobotnicím, které flashnuly a přičtení počítadla
        energy[f] = 0
        flashes += 1
    run += 1
    if run == 100:
        print("Part 1:", flashes)
    if np.sum(energy) == 0:
        print("Part 2:", run)
        break
