import numpy as np
# maska pro čtyřokolí 3x3 submatice
mask = np.array([[False, True, False], [True, True, True], [False, True, False]])

with open("input.txt", "r") as f:
    heights = [list(x.strip()) for x in f.readlines()]
matrix = np.array(heights, dtype=np.int8)
# výplň pomocí 9, abych nemusel řešit hranice matice a body přesto korektně vycházely
matrix = np.pad(matrix, pad_width=1, mode="constant", constant_values=9)
ymax, xmax = matrix.shape
risk = 0    # suma risk-levelu
basin_seeds = []    # seedy pro part 2
for y in range(1,ymax-1):
    for x in range(1,xmax-1):
        submat = matrix[y-1:y+2, x-1:x+2]   # 3x3 submatice
        submat = submat[mask]   # maskování matice od rohových bodů (skenujeme čtyřokolí)
        value = matrix[y, x]
        # pokud je zkoumená (uprostřed) hodnota ze submatice nejmenší a není 9, pak je lokálně nejnižším bodem
        if value == min(submat) and value != 9:
            risk += 1+value
            basin_seeds.append((y,x))
print("Part 1:", risk)

flood_stack = []    # zásobník pro další body k rozvoji čtyřokolí
basins = []         # seznam nalezených kotlin
for seed in basin_seeds:
    flood_stack.append(seed)     # inicializace zásobníku jedním z lokálně nejnižších bodů z part 1
    basin = 0
    while len(flood_stack) > 0:
        point = flood_stack.pop()
        if matrix[point] != 9 and matrix[point] != -1:  # 9 - hranice, -1 - prozkoumaný bod
            matrix[point] = -1      # označím jako prozkoumaný
            flood_stack.append((point[0], point[1] + 1))    # vložím do zásobníku čtyřokolí bodu
            flood_stack.append((point[0] + 1, point[1]))
            flood_stack.append((point[0], point[1] - 1))
            flood_stack.append((point[0] - 1, point[1]))
            basin += 1
    basins.append(basin)
top3 = sorted(basins, reverse=True)[:3]  # vezmu jen 3 největší (podle zadání)
print("Part 2:", top3[0]*top3[1]*top3[2])