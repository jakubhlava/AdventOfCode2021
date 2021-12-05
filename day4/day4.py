import numpy as np
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

called_numbers = [int(x) for x in lines[0].split(",")]
boards = []  # seznam matic s hracími poli
board = []   # pracovní pole pro tvorbu matice z tádků souboru
counter = 0
for ln in range(2, len(lines)):  # skip čísel na začátku
    if lines[ln] != "":
        board.append([int(x) for x in lines[ln].split()])
    if lines[ln] == "" or ln == len(lines)-1:
        npboard = np.array(board, dtype=np.int32)
        boards.append({"id": counter, "board": npboard})  # označkování kvůli part 2
        counter += 1
        board = []

winner, loser = None, None
already_won = set()

for num in called_numbers:
    board_list = [b for b in boards if b["id"] not in already_won]
    for b in board_list:
        b["board"][b["board"] == num] = -1  # všechny políčka s číslem nahradíme -1, abychom poznali výherní řádek
        if True in np.all(b["board"] == -1, axis=0) or True in np.all(b["board"] == -1, axis=1):
            if winner is None:
                winner = num*np.clip(b["board"], 0, None).sum()  # np.clip v kopii pole odstraní -1 a nahradí je 0
            already_won.add(b["id"])
    if len(board_list) == 1:  # zbývá poslední deska, "proherní"
        loser = num*np.clip(board_list[0]["board"], 0, None).sum()

print(f"Part 1: {winner}")
print(f"Part 2: {loser}")
