import numpy as np
import time

def neighbors(x, y, matrix):
    """Čtyřokolí daného bodu v matici"""
    n = []
    if x > 0:
        n.append((x-1, y))
    if x < matrix.shape[1]-1:
        n.append((x+1, y))
    if y > 0:
        n.append((x, y-1))
    if y < matrix.shape[0]-1:
        n.append((x, y+1))
    return n

def linear(point, matrix):
    """Linearizuje tuple s bodem v matici kvůli použití v hashovaných typech set adict"""
    return point[0] * matrix.shape[1] + point[1]

def pt(linear, matrix):
    """Reverzní funkce k linear"""
    return (linear // matrix.shape[1], linear % matrix.shape[1])

def extract_min(unvisited, dijkstra):
    """Najde nejlepší (s nejmenší cenou přechodu od známých) vrchol pro pokračování hledání cesty"""
    min = np.iinfo(np.int32).max
    mp = None
    for u in unvisited:
        point = pt(u, dijkstra)
        if dijkstra[point] < min:
            min = dijkstra[point]
            mp = point
    return mp

def add_with_wrap(x):
    """Implementace wrapu podle zadání, modulo nestačí"""
    if x == 9:
        return 1
    else:
        return x + 1

def compute_dijkstra(matrix, target):
    """Modifikovaná implementace dijkstrova algoritmu s vyřazením netknutých bodů z hledání nejlepšího vrcholu extract_min"""
    dijkstra = np.ndarray(matrix.shape, dtype=np.int32)
    dijkstra[:] = np.iinfo(np.int32).max    # místo nekonečna maximánlí hodnota int32

    unvis_touched = {0}  # nenavštívené modifikované
    previous = {}        # slovník s předky jednotlivých bodů
    dijkstra[(0, 0)] = 0  # první pole má nulovou cenu přechodu - začínáme zde
    while unvis_touched:
        best = extract_min(unvis_touched, dijkstra)     # hledání nejlepšího vrcholu
        unvis_touched.remove(linear(best, matrix))      # odstranění z množiny nenavštívených
        for n in neighbors(*best, matrix):              # přehodnocení sousedů
            if dijkstra[best] + matrix[n] < dijkstra[n]:
                dijkstra[n] = dijkstra[best] + matrix[n]
                previous[linear(n, matrix)] = best
                unvis_touched.add(linear(n, matrix))
        if best[0] == target[0] and best[1] == target[1]:
            break
    return dijkstra

addrisk = np.vectorize(add_with_wrap)  # vektorizace funkce pro zjednodušení práce s maticí

with open("input.txt", "r") as f:
    risks = [[int(x) for x in l.strip()] for l in f.readlines()]

matrix = np.array(risks)

begin = (0, 0)
target = (matrix.shape[0]-1, matrix.shape[1]-1)

print("Part 1:", compute_dijkstra(matrix, target)[target])

# rozšíření matice 5x do každé strany se zvýšením risků podle part2 zadání
appendmatrix = addrisk(matrix)
for _ in range(4):
    matrix = np.append(matrix, appendmatrix, 0)
    appendmatrix = addrisk(appendmatrix)

appendmatrix = addrisk(matrix)
for _ in range(4):
    matrix = np.append(matrix, appendmatrix, 1)
    appendmatrix = addrisk(appendmatrix)

target = (matrix.shape[0]-1, matrix.shape[1]-1)

print("Computing part 2... please wait (may take minute or two...)")
print("Part 2:", compute_dijkstra(matrix, target)[target])




