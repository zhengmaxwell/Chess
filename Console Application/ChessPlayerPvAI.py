from MoveEval import *
import time

human = black
computer = white

board = default()
PrintBoard(board)
print("Black has first move.")

status = True
white = [10, 11, 12, 13, 14, 15]
black = [20, 21, 22, 23, 24, 25]

turn = 0
while status:

    pos = None
    new_pos = None
    if turn % 2 == 0:
        player = human
        print("Your turn")

        val = None
        while val not in player or GetPieceLegalMoves(board, pos) == []:
            row, col = input("Pick your piece: [y x] -> ").split()
            pos = GetPosition(int(row), int(col))
            val = board[pos]

        while new_pos not in GetPieceLegalMoves(board, pos):
            row, col = input("Pick where to move: [y x] -> ").split()
            new_pos = GetPosition(int(row), int(col))

        PrintBoard(makeMove(board, pos, new_pos))


    else:
        start = time.time()
        player = computer
        pos = minimax(board, player)[0][0]
        new_pos = minimax(board, player)[0][1]
        end = time.time()
        time_elapsed = end - start

        PrintBoard(makeMove(board, pos, new_pos))
        print("Time Elapsed: " + str("%.2f" % time_elapsed) + "\n")

    turn += 1

    if 15 not in board or 25 not in board:
        status = False

if 15 not in board:
    print("Congratulations Black")
elif 25 not in board:
    print("Congratulations White")
