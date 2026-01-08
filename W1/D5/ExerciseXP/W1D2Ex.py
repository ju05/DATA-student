def create_board():
    table = []
    for x in range(3):
        table.append([])
        for y in range(3):
            table[x].append(" ")
    return table


def display_board(*args):
    for a in args[0]:
        print('|'.join(a))


def player_input(player):
    position = ""
    while position != "q":
        position = input(f"{player} enter the position (x y) or 'q': ")
        if position == "q":
            break
        move = position.split()
        if len(move) != 2:
            print("Try again. Enter the position (x y) or 'q': ")
        elif not move[0].isnumeric() or not move[1].isnumeric():
            print("You should input only numbers!")
        elif 1 <= int(move[0]) <= 3 and 1 <= int(move[1]) <= 3:
            move_ok = [int(move[0]) - 1, int(move[1]) - 1]
            if table[move_ok[0]][move_ok[1]] == " ":
                return move_ok
            else:
                print("This field is occupied. Try again. Enter the position (x y) or 'q': ")
        else:
            print("Position must be between 1 to 3. Try again. Enter the position (x y) or 'q': ")
        display_board(table)


def check_win(player):
    c1 = 0
    c2 = 0
    for win_line in range(3):
        a = 0
        b = 0
        for win_raw in range(3):
            if table[win_line][win_raw] == players[player]:
                a += 1
            if table[win_raw][win_line] == players[player]:
                b += 1
        if a == 3 or b == 3:
            return player
    for diagonal in range(3):
        if table[diagonal][diagonal] == players[player]:
            c1 += 1
        if table[-diagonal-1][diagonal] == players[player]:
            c2 += 1
    if c1 == 3 or c2 == 3:
        return player


def tie():
    tie_counter = 0
    for tie_line in table:
        tie_counter += len(''.join(tie_line).replace(' ',''))
    if tie_counter == 9:
        return "tie"





table = create_board()
q = ""
players = {"Player1": "X", "Player2": "O"}
players_name = list(players.keys())
finish_game = ""
counter_moves = 0
player_turn = 0

while not finish_game:
    counter_moves += 1
    display_board(table)
    move_result = player_input(players_name[counter_moves%2])
    if move_result is None:
        print("Quit game")
        break
    if move_result:
        table[move_result[0]][move_result[1]] = players[players_name[counter_moves%2]]
    finish_game = check_win(players_name[counter_moves%2])
    if tie():
        print("It is tie")
        break
    if finish_game and not tie():
        display_board(table)
        print(f"{players_name[counter_moves%2]} is win")

