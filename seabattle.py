import random

cells = list(range(1, 50))  
board = [cells[i:i + 7] for i in range(0, len(cells), 7)]

banned_cells = []

def banned_cells_calculator(a):
    return banned_cells.extend([a, a - 1, a + 1, a - 8, a - 7, a - 6, a + 6, a + 7, a + 8])

# Spawning 1x ships
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
# Spawning 1x ships

# Spawning 2x ships
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
# Spawning 2x ships

# Spawning 3x ship
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
# Spawning 3x ship

print(ship1x_1, ship1x_2, ship1x_3, ship1x_4, ship2x_1, ship2x_2, ship3x)

def determine_cell(cell):
    column = cell[0].upper()  
    row = int(cell[1])  
    
    column_number = ord(column) - ord('A') + 1
    
    cell_number = (column_number - 1) * 7 + row
    return cell_number
all_ships = ship1x_1 + ship1x_2 + ship1x_3 + ship1x_4 + ship2x_1 + ship2x_2 + ship3x
taken_shots = []

print("Enter your name")
name = input()

guess_board = [[0] * 7 for _ in range(7)]
print("  A B C D E F G")
row_number = 1
for row in guess_board:
    print(row_number, end=" ")
    for elem in row:
        print(elem, end=" ")  
    row_number += 1
    print() 

print()

print("Take a shot. - is miss, + is hit, S is sunk")
shot = input()
while len(shot) != 2 or shot[0] not in "ABCDEFG" or shot[1] not in '1234567' or determine_cell(shot) in taken_shots:
    print("Invalid input or you have already shot this square. Try again")
    shot = input()

if determine_cell(shot) not in all_ships:
    guess_board[determine_cell(shot)] = "-"
else:
    guess_board[determine_cell(shot)] = "+"

if all(item in taken_shots for item in ship1x_1):
    guess_board[ship1x_1[0]] = "S"
if all(item in taken_shots for item in ship1x_2):
    guess_board[ship1x_2[0]] = "S"
if all(item in taken_shots for item in ship1x_3):
    guess_board[ship1x_3[0]] = "S"
if all(item in taken_shots for item in ship1x_4):
    guess_board[ship1x_4[0]] = "S"

if all(item in taken_shots for item in ship2x_1):
    guess_board[ship2x_1[0]] = "S"
    guess_board[ship2x_1[1]] = "S"
if all(item in taken_shots for item in ship2x_2):
    guess_board[ship2x_2[0]] = "S"
    guess_board[ship2x_2[1]] = "S"

if all(item in taken_shots for item in ship3x):
    guess_board[ship3x[0]] = "S"
    guess_board[ship3x[1]] = "S"
    guess_board[ship3x[2]] = "S"

print("  A B C D E F G")
row_number = 1
for row in guess_board:
    print(row_number, end=" ")
    for elem in row:
        print(elem, end=" ")  
    row_number += 1
    print()