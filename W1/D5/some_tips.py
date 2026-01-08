board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

# Each position could be a number from 1 to 9
def check_win():
    win_coor = ((0, 1, 3), (3, 4, 5), (6,7,8), (0, 3, 6), (1, 4, 7), (2,5,8),(0,4,8))
    global game_goes_on

    for coord in win_coor:
        if board[coord[0]] == board[coord[1]] == board[coord[2]] != "-":
            winner = board[coord[0]]
            game_goes_on = False
            return winner