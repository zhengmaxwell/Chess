pawn = [10, 20]
knight = [11, 21]
bishop = [12, 22]
rook = [13, 23]
queen = [14, 24]
king = [15, 25]

white = [10, 11, 12, 13, 14, 15]
black = [20, 21, 22, 23, 24, 25]

pieces = {20 : "♟", 21 : "♞", 22 : "♝", 23 : "♜", 24 : "♛", 25 : "♚", 10: "♙", 11 : "♘", 12 : "♗", 13 : "♖", 14 : "♕", 15 : "♔", "test" : "★"}

row0 = range(0, 8)
row1 = range(8, 16)
row2 = range(16, 24)
row3 = range(24, 32)
row4 = range(32, 40)
row5 = range(40, 48)
row6 = range(48, 56)
row7 = range(56, 64)

rows = [row0, row1, row2, row3, row4, row5, row6, row7]


def GetRowCol(position):

    output_row = position // 8
    output_col = position % 8
    return output_row, output_col


def GetPosition(row, col):

    return row*8 + col

def default():

    return [13, 11, 12, 14, 15, 12, 11, 13] + [10] * 8 + [0] * 32 + [20] * 8 + [23, 21, 22, 24, 25, 22, 21, 23]


def PrintBoard(board):

    output_rows = []
    j = 7
    for row in rows[::-1]:
        output = ""
        for i in range(len(board)):
            if i in row:
                row_index = rows.index(row)
                if board[i] == 0:
                    if row_index % 2 == 0:
                        if i % 2 == 0:
                            output += " - "
                        else:
                            output += "   "
                    else:
                        if i % 2 == 0:
                            output += "   "
                        else:
                            output += " - "
                else:
                    output += " " + pieces[board[i]] + " "

        output = str(j) + " ║ " + output + " ║ "
        output_rows.append(output)
        j -= 1

    print("  ╔══════════════════════════╗")
    for row in output_rows:
        print(row)
    print("  ╚══════════════════════════╝")
    print("     0  1  2  3  4  5  6  7 ")