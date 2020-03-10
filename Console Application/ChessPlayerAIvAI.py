from MoveEval import *
import time


board = default()
PrintBoard(board)
print("White has first move.")

status = True
white = [10, 11, 12, 13, 14, 15]
black = [20, 21, 22, 23, 24, 25]

comp1 = white
comp2 = black

turn = 0
while status:

    if turn % 2 == 0:
        player = comp1
        print("White Turn")
    else:
        player = comp2
        print("Black Turn")

    start = time.time()
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
