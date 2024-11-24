import random
import os

cells = list(range(1, 50))  
board = [cells[i:i + 7] for i in range(0, len(cells), 7)]
another_game = "YES"
scores = []
names = []

def banned_cells_calculator(a):
    return banned_cells.extend([a, a - 1, a + 1, a - 8, a - 7, a - 6, a + 6, a + 7, a + 8])

def determine_cell(cell):
    column = ord(cell[0].upper()) - ord('A') + 1
    row = int(cell[1])
    return (row - 1) * 7 + column

while another_game == "YES":
    banned_cells = []
    taken_shots = []
    
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

    print(ship1x_1, ship1x_2, ship1x_3, ship1x_4, ship2x_1, ship2x_2, ship3x)
    
    print()
    
    all_ships = ship1x_1 + ship1x_2 + ship1x_3 + ship1x_4 + ship2x_1 + ship2x_2 + ship3x
    
    print("Enter your name")
    name = input()
    names.append(name)

    guess_board = [[0] * 7 for _ in range(7)]
    print("  A B C D E F G")
    row_number = 1
    for row in guess_board:
        print(row_number, end=" ")
        for elem in row:
            print(elem, end=" ")
        print()
        row_number += 1

    while all(item in taken_shots for item in all_ships) == False:
        print()
        print("Take a shot. + is hit, - is miss, S is sunk")
        shot = input()
        while len(shot) != 2 or shot[0] not in "ABCDEFG" or shot[1] not in "1234567":
            print("You shot this square before or you've made a mistake. Try again")
            shot = input()
        taken_shots.append(determine_cell(shot))
        
        if determine_cell(shot) in all_ships and 1 <= determine_cell(shot) <= 7:
            guess_board[0][determine_cell(shot) - 1] = "+"
        elif determine_cell(shot) in all_ships and 8 <= determine_cell(shot) <= 14:
            guess_board[1][determine_cell(shot) - 8] = "+"
        elif determine_cell(shot) in all_ships and 15 <= determine_cell(shot) <= 21:
            guess_board[2][determine_cell(shot) - 15] = "+"
        elif determine_cell(shot) in all_ships and 22 <= determine_cell(shot) <= 28:
            guess_board[3][determine_cell(shot) - 22] = "+"
        elif determine_cell(shot) in all_ships and 29 <= determine_cell(shot) <= 35:
            guess_board[4][determine_cell(shot) - 29] = "+"
        elif determine_cell(shot) in all_ships and 36 <= determine_cell(shot) <= 42:
            guess_board[5][determine_cell(shot) - 36] = "+"
        elif determine_cell(shot) in all_ships and 43 <= determine_cell(shot) <= 49:
            guess_board[6][determine_cell(shot) - 43] = "+"

        if determine_cell(shot) not in all_ships and 1 <= determine_cell(shot) <= 7:
            guess_board[0][determine_cell(shot) - 1] = "-"
        elif determine_cell(shot) not in all_ships and 8 <= determine_cell(shot) <= 14:
            guess_board[1][determine_cell(shot) - 8] = "-"
        elif determine_cell(shot) not in all_ships and 15 <= determine_cell(shot) <= 21:
            guess_board[2][determine_cell(shot) - 15] = "-"
        elif determine_cell(shot) not in all_ships and 22 <= determine_cell(shot) <= 28:
            guess_board[3][determine_cell(shot) - 22] = "-"
        elif determine_cell(shot) not in all_ships and 29 <= determine_cell(shot) <= 35:
            guess_board[4][determine_cell(shot) - 29] = "-"
        elif determine_cell(shot) not in all_ships and 36 <= determine_cell(shot) <= 42:
            guess_board[5][determine_cell(shot) - 36] = "-"
        elif determine_cell(shot) not in all_ships and 43 <= determine_cell(shot) <= 49:
            guess_board[6][determine_cell(shot) - 43] = "-"

        if all(item in taken_shots for item in ship1x_1) and 1 <= ship1x_1[0] <= 7:
            guess_board[0][ship1x_1[0] - 1] = "S"
        elif all(item in taken_shots for item in ship1x_1) and 8 <= ship1x_1[0] <= 14:
            guess_board[1][ship1x_1[0] - 8] = "S"
        elif all(item in taken_shots for item in ship1x_1) and 15 <= ship1x_1[0] <= 21:
            guess_board[2][ship1x_1[0] - 15] = "S"
        elif all(item in taken_shots for item in ship1x_1) and 22 <= ship1x_1[0] <= 28:
            guess_board[3][ship1x_1[0] - 22] = "S"
        elif all(item in taken_shots for item in ship1x_1) and 29 <= ship1x_1[0] <= 35:
            guess_board[4][ship1x_1[0] - 29] = "S"
        elif all(item in taken_shots for item in ship1x_1) and 36 <= ship1x_1[0] <= 42:
            guess_board[5][ship1x_1[0] - 36] = "S"
        elif all(item in taken_shots for item in ship1x_1) and 43 <= ship1x_1[0] <= 49:
            guess_board[6][ship1x_1[0] - 43] = "S"

        if all(item in taken_shots for item in ship1x_2) and 1 <= ship1x_2[0] <= 7:
            guess_board[0][ship1x_2[0] - 1] = "S"
        elif all(item in taken_shots for item in ship1x_2) and 8 <= ship1x_2[0] <= 14:
            guess_board[1][ship1x_2[0] - 8] = "S"
        elif all(item in taken_shots for item in ship1x_2) and 15 <= ship1x_2[0] <= 21:
            guess_board[2][ship1x_2[0] - 15] = "S"
        elif all(item in taken_shots for item in ship1x_2) and 22 <= ship1x_2[0] <= 28:
            guess_board[3][ship1x_2[0] - 22] = "S"
        elif all(item in taken_shots for item in ship1x_2) and 29 <= ship1x_2[0] <= 35:
            guess_board[4][ship1x_2[0] - 29] = "S"
        elif all(item in taken_shots for item in ship1x_2) and 36 <= ship1x_2[0] <= 42:
            guess_board[5][ship1x_2[0] - 36] = "S"
        elif all(item in taken_shots for item in ship1x_2) and 43 <= ship1x_2[0] <= 49:
            guess_board[6][ship1x_2[0] - 43] = "S"

        if all(item in taken_shots for item in ship1x_3) and 1 <= ship1x_3[0] <= 7:
            guess_board[0][ship1x_3[0] - 1] = "S"
        elif all(item in taken_shots for item in ship1x_3) and 8 <= ship1x_3[0] <= 14:
            guess_board[1][ship1x_3[0] - 8] = "S"
        elif all(item in taken_shots for item in ship1x_3) and 15 <= ship1x_3[0] <= 21:
            guess_board[2][ship1x_3[0] - 15] = "S"
        elif all(item in taken_shots for item in ship1x_3) and 22 <= ship1x_3[0] <= 28:
            guess_board[3][ship1x_3[0] - 22] = "S"
        elif all(item in taken_shots for item in ship1x_3) and 29 <= ship1x_3[0] <= 35:
            guess_board[4][ship1x_3[0] - 29] = "S"
        elif all(item in taken_shots for item in ship1x_3) and 36 <= ship1x_3[0] <= 42:
            guess_board[5][ship1x_3[0] - 36] = "S"
        elif all(item in taken_shots for item in ship1x_3) and 43 <= ship1x_3[0] <= 49:
            guess_board[6][ship1x_3[0] - 43] = "S"

        if all(item in taken_shots for item in ship1x_4) and 1 <= ship1x_4[0] <= 7:
            guess_board[0][ship1x_4[0] - 1] = "S"
        elif all(item in taken_shots for item in ship1x_4) and 8 <= ship1x_4[0] <= 14:
            guess_board[1][ship1x_4[0] - 8] = "S"
        elif all(item in taken_shots for item in ship1x_4) and 15 <= ship1x_4[0] <= 21:
            guess_board[2][ship1x_4[0] - 15] = "S"
        elif all(item in taken_shots for item in ship1x_4) and 22 <= ship1x_4[0] <= 28:
            guess_board[3][ship1x_4[0] - 22] = "S"
        elif all(item in taken_shots for item in ship1x_4) and 29 <= ship1x_4[0] <= 35:
            guess_board[4][ship1x_4[0] - 29] = "S"
        elif all(item in taken_shots for item in ship1x_4) and 36 <= ship1x_4[0] <= 42:
            guess_board[5][ship1x_4[0] - 36] = "S"
        elif all(item in taken_shots for item in ship1x_4) and 43 <= ship1x_4[0] <= 49:
            guess_board[6][ship1x_4[0] - 43] = "S"

        if all(item in taken_shots for item in ship2x_1) and 1 <= ship2x_1[0] <= 7:
            guess_board[0][ship2x_1[0] - 1] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 8 <= ship2x_1[0] <= 14:
            guess_board[1][ship2x_1[0] - 8] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 15 <= ship2x_1[0] <= 21:
            guess_board[2][ship2x_1[0] - 15] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 22 <= ship2x_1[0] <= 28:
            guess_board[3][ship2x_1[0] - 22] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 29 <= ship2x_1[0] <= 35:
            guess_board[4][ship2x_1[0] - 29] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 36 <= ship2x_1[0] <= 42:
            guess_board[5][ship2x_1[0] - 36] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 43 <= ship2x_1[0] <= 49:
            guess_board[6][ship2x_1[0] - 43] = "S"
        if all(item in taken_shots for item in ship2x_1) and 1 <= ship2x_1[1] <= 7:
            guess_board[0][ship2x_1[1] - 1] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 8 <= ship2x_1[1] <= 14:
            guess_board[1][ship2x_1[1] - 8] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 15 <= ship2x_1[1] <= 21:
            guess_board[2][ship2x_1[1] - 15] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 22 <= ship2x_1[1] <= 28:
            guess_board[3][ship2x_1[1] - 22] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 29 <= ship2x_1[1] <= 35:
            guess_board[4][ship2x_1[1] - 29] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 36 <= ship2x_1[1] <= 42:
            guess_board[5][ship2x_1[1] - 36] = "S"
        elif all(item in taken_shots for item in ship2x_1) and 43 <= ship2x_1[1] <= 49:
            guess_board[6][ship2x_1[1] - 43] = "S"

        if all(item in taken_shots for item in ship2x_2) and 1 <= ship2x_2[0] <= 7:
            guess_board[0][ship2x_2[0] - 1] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 8 <= ship2x_2[0] <= 14:
            guess_board[1][ship2x_2[0] - 8] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 15 <= ship2x_2[0] <= 21:
            guess_board[2][ship2x_2[0] - 15] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 22 <= ship2x_2[0] <= 28:
            guess_board[3][ship2x_2[0] - 22] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 29 <= ship2x_2[0] <= 35:
            guess_board[4][ship2x_2[0] - 29] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 36 <= ship2x_2[0] <= 42:
            guess_board[5][ship2x_2[0] - 36] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 43 <= ship2x_2[0] <= 49:
            guess_board[6][ship2x_2[0] - 43] = "S"
        if all(item in taken_shots for item in ship2x_2) and 1 <= ship2x_2[1] <= 7:
            guess_board[0][ship2x_2[1] - 1] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 8 <= ship2x_2[1] <= 14:
            guess_board[1][ship2x_2[1] - 8] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 15 <= ship2x_2[1] <= 21:
            guess_board[2][ship2x_2[1] - 15] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 22 <= ship2x_2[1] <= 28:
            guess_board[3][ship2x_2[1] - 22] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 29 <= ship2x_2[1] <= 35:
            guess_board[4][ship2x_2[1] - 29] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 36 <= ship2x_2[1] <= 42:
            guess_board[5][ship2x_2[1] - 36] = "S"
        elif all(item in taken_shots for item in ship2x_2) and 43 <= ship2x_2[1] <= 49:
            guess_board[6][ship2x_2[1] - 43] = "S"

        if all(item in taken_shots for item in ship3x) and 1 <= ship3x[0] <= 7:
            guess_board[0][ship3x[0] - 1] = "S"
        elif all(item in taken_shots for item in ship3x) and 8 <= ship3x[0] <= 14:
            guess_board[1][ship3x[0] - 8] = "S"
        elif all(item in taken_shots for item in ship3x) and 15 <= ship3x[0] <= 21:
            guess_board[2][ship3x[0] - 15] = "S"
        elif all(item in taken_shots for item in ship3x) and 22 <= ship3x[0] <= 28:
            guess_board[3][ship3x[0] - 22] = "S"
        elif all(item in taken_shots for item in ship3x) and 29 <= ship3x[0] <= 35:
            guess_board[4][ship3x[0] - 29] = "S"
        elif all(item in taken_shots for item in ship3x) and 36 <= ship3x[0] <= 42:
            guess_board[5][ship3x[0] - 36] = "S"
        elif all(item in taken_shots for item in ship3x) and 43 <= ship3x[0] <= 49:
            guess_board[6][ship3x[0] - 43] = "S"
        if all(item in taken_shots for item in ship3x) and 1 <= ship3x[1] <= 7:
            guess_board[0][ship3x[1] - 1] = "S"
        elif all(item in taken_shots for item in ship3x) and 8 <= ship3x[1] <= 14:
            guess_board[1][ship3x[1] - 8] = "S"
        elif all(item in taken_shots for item in ship3x) and 15 <= ship3x[1] <= 21:
            guess_board[2][ship3x[1] - 15] = "S"
        elif all(item in taken_shots for item in ship3x) and 22 <= ship3x[1] <= 28:
            guess_board[3][ship3x[1] - 22] = "S"
        elif all(item in taken_shots for item in ship3x) and 29 <= ship3x[1] <= 35:
            guess_board[4][ship3x[1] - 29] = "S"
        elif all(item in taken_shots for item in ship3x) and 36 <= ship3x[1] <= 42:
            guess_board[5][ship3x[1] - 36] = "S"
        elif all(item in taken_shots for item in ship3x) and 43 <= ship3x[1] <= 49:
            guess_board[6][ship3x[1] - 43] = "S"
        if all(item in taken_shots for item in ship3x) and 1 <= ship3x[2] <= 7:
            guess_board[0][ship3x[2] - 1] = "S"
        elif all(item in taken_shots for item in ship3x) and 8 <= ship3x[2] <= 14:
            guess_board[1][ship3x[2] - 8] = "S"
        elif all(item in taken_shots for item in ship3x) and 15 <= ship3x[2] <= 21:
            guess_board[2][ship3x[2] - 15] = "S"
        elif all(item in taken_shots for item in ship3x) and 22 <= ship3x[2] <= 28:
            guess_board[3][ship3x[2] - 22] = "S"
        elif all(item in taken_shots for item in ship3x) and 29 <= ship3x[2] <= 35:
            guess_board[4][ship3x[2] - 29] = "S"
        elif all(item in taken_shots for item in ship3x) and 36 <= ship3x[2] <= 42:
            guess_board[5][ship3x[2] - 36] = "S"
        elif all(item in taken_shots for item in ship3x) and 43 <= ship3x[2] <= 49:
            guess_board[6][ship3x[2] - 43] = "S"

        os.system('cls' if os.name == 'nt' else 'clear')

        print("  A B C D E F G")
        row_number = 1
        for row in guess_board:
            print(row_number, end=" ")
            for elem in row:
                print(elem, end=" ")
            print()
            row_number += 1

    scores.append(len(taken_shots))
    print("You've won. Do you want to start another game? Enter YES or NO")
    another_game = input()

print("Scoreboard")
players = list(zip(names, scores))
players.sort(key=lambda x: x[1])
for idx, (user, shots) in enumerate(players, start=1):
    print(f"Place {idx}: {user} - {shots} shots")