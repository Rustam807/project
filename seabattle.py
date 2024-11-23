import random

cells = list(range(1, 50))  
board = [cells[i:i + 7] for i in range(0, len(cells), 7)]

banned_cells = []

def banned_cells_calculator(a):
    return banned_cells.extend([a, a - 1, a + 1, a - 8, a - 7, a - 6, a + 6, a + 7, a + 8])

ship3x = [random.randint(1, 49)]
while ship3x[0] in banned_cells:
    ship3x = [random.randint(1, 49)]
if ship3x[0] + 7 not in banned_cells and ship3x[0] + 7 in cells:
    ship3x.append(ship3x[0] + 7)
elif ship3x[0] - 7 not in banned_cells and ship3x[0] - 7 in cells:
    ship3x.append(ship3x[0] - 7)
elif ship3x[0] + 1 not in banned_cells and ship3x[0] + 1 in cells:
    ship3x.append(ship3x[0] + 1)
elif ship3x[0] - 1 not in banned_cells and ship3x[0] - 1 in cells:
    ship3x.append(ship3x[0] - 1)
if ship3x[1] + 7 not in banned_cells and ship3x[1] + 7 in cells:
    ship3x.append(ship3x[1] + 7)
elif ship3x[1] - 7 not in banned_cells and ship3x[1] - 7 in cells:
    ship3x.append(ship3x[1] - 7)
elif ship3x[1] + 1 not in banned_cells and ship3x[1] + 1 in cells:
    ship3x.append(ship3x[1] + 1)
elif ship3x[1] - 1 not in banned_cells and ship3x[1] - 1 in cells:
    ship3x.append(ship3x[1] - 1)
banned_cells_calculator(ship3x[0])
banned_cells_calculator(ship3x[1])
banned_cells_calculator(ship3x[2])

ship2x_1 = [random.randint(1, 49)]
while ship2x_1[0] in banned_cells:
    ship2x_1 = [random.randint(1, 49)]
if ship2x_1[0] + 7 not in banned_cells and ship2x_1[0] + 7 in cells:
    ship2x_1.append(ship2x_1[0] + 7)
elif ship2x_1[0] - 7 not in banned_cells and ship2x_1[0] - 7 in cells:
    ship2x_1.append(ship2x_1[0] - 7)
elif ship2x_1[0] + 1 not in banned_cells and ship2x_1[0] + 1 in cells:
    ship2x_1.append(ship2x_1[0] + 1)
elif ship2x_1[0] - 1 not in banned_cells and ship2x_1[0] - 1 in cells:
    ship2x_1.append(ship2x_1[0] - 1)
banned_cells_calculator(ship2x_1[0])
banned_cells_calculator(ship2x_1[1])

ship2x_2 = [random.randint(1, 49)]
while ship2x_2[0] in banned_cells:
    ship2x_2 = [random.randint(1, 49)]
if ship2x_2[0] + 7 not in banned_cells and ship2x_2[0] + 7 in cells:
    ship2x_2.append(ship2x_2[0] + 7)
elif ship2x_2[0] - 7 not in banned_cells and ship2x_2[0] - 7 in cells:
    ship2x_2.append(ship2x_2[0] - 7)
elif ship2x_2[0] + 1 not in banned_cells and ship2x_2[0] + 1 in cells:
    ship2x_2.append(ship2x_2[0] + 1)
elif ship2x_2[0] - 1 not in banned_cells and ship2x_2[0] - 1 in cells:
    ship2x_2.append(ship2x_2[0] - 1)
banned_cells_calculator(ship2x_2[0])
banned_cells_calculator(ship2x_2[1])

ship1x_1 = [random.randint(1, 49)]
banned_cells_calculator(ship1x_1[0])

ship1x_2 = [random.randint(1, 49)]
while ship1x_2[0] in banned_cells:
    ship1x_2 = [random.randint(1, 49)]
banned_cells_calculator(ship1x_2[0])

ship1x_3 = [random.randint(1, 49)]
while ship1x_3[0] in banned_cells:
    ship1x_3 = [random.randint(1, 49)]
banned_cells_calculator(ship1x_3[0])

ship1x_4 = [random.randint(1, 49)]
while ship1x_4[0] in banned_cells:
    ship1x_4 = [random.randint(1, 49)]
banned_cells_calculator(ship1x_4[0])

print(ship1x_1, ship1x_2, ship1x_3, ship1x_4, ship2x_1, ship2x_2, ship3x)