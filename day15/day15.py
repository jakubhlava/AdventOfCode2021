import numpy as np
import time

def neighbors(x, y, matrix):
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
    return point[0] * matrix.shape[1] + point[1]

def pt(linear, matrix):
    return (linear // matrix.shape[1], linear % matrix.shape[1])

def extract_min(unvisited, dijkstra):
    min = np.iinfo(np.int32).max
    mp = None
    for u in unvisited:
        point = pt(u, dijkstra)
        if dijkstra[point] < min:
            min = dijkstra[point]
            mp = point
    return mp

def add_with_wrap(x):
    if x == 9:
        return 1
    else:
        return x + 1

def compute_dijkstra(matrix, target):
    dijkstra = np.ndarray(matrix.shape, dtype=np.int32)
    dijkstra[:] = np.iinfo(np.int32).max

    unvis_touched = {0}
    previous = {}
    dijkstra[(0, 0)] = 0
    #unvisited = {tuple(x) for x in np.argwhere(dijkstra == np.iinfo(np.int32).max)}
    i = 0
    t = time.time()
    while unvis_touched:
        i += 1
        if i%1000 == 0:
            print(i)
        best = extract_min(unvis_touched, dijkstra)
        unvis_touched.remove(linear(best, matrix))
        for n in neighbors(*best, matrix):
            if dijkstra[best] + matrix[n] < dijkstra[n]:
                dijkstra[n] = dijkstra[best] + matrix[n]
                previous[linear(n, matrix)] = best
                unvis_touched.add(linear(n, matrix))
        if best[0] == target[0] and best[1] == target[1]:
            break
    return dijkstra

addrisk = np.vectorize(add_with_wrap)

with open("input.txt", "r") as f:
    risks = [[int(x) for x in l.strip()] for l in f.readlines()]

matrix = np.array(risks)

begin = (0, 0)
target = (matrix.shape[0]-1, matrix.shape[1]-1)

print("Part 1:", compute_dijkstra(matrix, target)[target])

appendmatrix = addrisk(matrix)
for _ in range(4):
    matrix = np.append(matrix, appendmatrix, 0)
    appendmatrix = addrisk(appendmatrix)

appendmatrix = addrisk(matrix)
for _ in range(4):
    matrix = np.append(matrix, appendmatrix, 1)
    appendmatrix = addrisk(appendmatrix)

target = (matrix.shape[0]-1, matrix.shape[1]-1)

print("Part 2:", compute_dijkstra(matrix, target)[target])




