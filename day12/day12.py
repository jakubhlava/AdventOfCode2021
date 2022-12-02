import copy
import string

caves = {}
paths = []


class Cave:
    def __init__(self, name):
        self.name = name
        self.size = "big" if name[0] in string.ascii_uppercase else "small"
        self.visited = False
        self.children: set[str] = set()
        self.start = self.name == "start"
        self.end = self.name == "end"

    def __repr__(self):
        return f"CAVE: {self.name}"

    def __str__(self):
        return self.name

    def add_child(self, cave):
        if not cave.start:
            self.children.add(cave.name)


def make_step(next: Cave, path: list, small_visited: set):
    global caves
    paths = []
    path.append(next.name)
    if next.end:
        paths.append(path)
        return paths
    if not next.children:
        return []
    if next.size == "small":
        small_visited.add(next.name)
    for child in next.children:
        if child not in small_visited:
            paths.extend(make_step(caves[child], copy.deepcopy(path), copy.deepcopy(small_visited)))
    return paths


with open("input-sm.txt", "r") as f:
    ways = [w.strip().split("-") for w in f.readlines()]


for w in ways:
    for c in w:
        if c not in [str(cave) for cave in caves]:
            caves[c] = Cave(c)
    caves[w[0]].add_child(caves[w[1]])
    caves[w[1]].add_child(caves[w[0]])

paths = make_step(caves["start"], [], set())
print(len(paths))


