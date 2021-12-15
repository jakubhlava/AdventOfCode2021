import numpy as np

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
        if dijkstra[u] < min:
            min = dijkstra[u]
            mp = u
    return mp

with open("input.txt", "r") as f:
    risks = [[int(x) for x in l.strip()] for l in f.readlines()]

matrix = np.array(risks)

begin = (0, 0)
target = (matrix.shape[0]-1, matrix.shape[1]-1)

dijkstra = np.ndarray(matrix.shape, dtype=np.int32)
dijkstra[:] = np.iinfo(np.int32).max


unvisited = [tuple(x) for x in np.argwhere(dijkstra == np.iinfo(np.int32).max)]
previous = {}
dijkstra[(0,0)] = 0
while unvisited:
    best = extract_min(unvisited, dijkstra)
    unvisited.remove(best)
    for n in neighbors(*best, matrix):
        if dijkstra[best] + matrix[n] < dijkstra[n]:
            dijkstra[n] = dijkstra[best] + matrix[n]
            previous[linear(n, matrix)] = best

print("Part 1:", dijkstra[target])

