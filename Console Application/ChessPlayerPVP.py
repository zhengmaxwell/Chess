from MoveGen import *


board = default()
PrintBoard(board)
print("White has first move.")

status = True
white = [10, 11, 12, 13, 14, 15]
black = [20, 21, 22, 23, 24, 25]

turn = 0
while status:
    if turn % 2 == 0:
        player = white
        print("White Turn")
    else:
        player = black
        print("Black Turn")

    val = None
    pos = None
    while val not in player or GetPieceLegalMoves(board, pos) == []:
        row, col = input("Pick your piece: [y x] -> ").split()
        pos = GetPosition(int(row), int(col))
        val = board[pos]

    new_pos = None
    while new_pos not in GetPieceLegalMoves(board, pos):
        row, col = input("Pick where to move: [y x] -> ").split()
        new_pos = GetPosition(int(row), int(col))

    PrintBoard(makeMove(board, pos, new_pos))
    turn += 1

    if 15 not in board or 25 not in board:
        status = False

if 15 not in board:
    print("Congratulations Black")
elif 25 not in board:
    print("Congratulations White")





