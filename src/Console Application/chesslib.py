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

print('gai')

def GetRowCol(position):

    output_row = output_col = None

    for row in rows:
        if position in row:
            output_row = rows.index(row)
            for i in range(len(row)):
                if position == row[i]:
                    output_col = i

    return output_row, output_col


def GetPosition(row, col):

    return row*8 + col

def Default():

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
                            output += " # "
                    else:
                        if i % 2 == 0:
                            output += " # "
                        else:
                            output += " - "
                else:
                    output += " " + pieces[board[i]] + " "

        output = str(j) + " ║ " + output + " ║"
        output_rows.append(output)
        j -= 1

    print("  ╔══════════════════════════╗")
    for row in output_rows:
        print(row)
    print("  ╚══════════════════════════╝")
    print("     0  1  2  3  4  5  6  7 ")



def GetPlayerPositions(board, player):

    output = []
    for val in board:
        if player == 10:
            if val in white:
                output.append(board.index(val))
        elif player == 20:
            if val in black:
                output.append(board.index(val))

    return output


def GetPieceLegalMoves(board, position):

    output = []
    row = GetRowCol(position)[0]
    col = GetRowCol(position)[1]

    up = row + 1
    down = row - 1
    right = col + 1
    left = col - 1

    if board[position] in white:
        player = white
        opposition = black
    elif board[position] in black:
        player = black
        opposition = white
    else:
        return None

    if board[position] in pawn:

        if board[position] in white:
            if row == 7:
                board[position] = 14
                return GetPieceLegalMoves(board, position)

            if board[position + 8] == 0:
                output.append(position + 8)

            if col != 7:
                if board[GetPosition(row + 1, col + 1)] in opposition:
                    output.append(GetPosition(row + 1, col + 1))
            if col != 0:
                if board[GetPosition(row + 1, col - 1)] in opposition:
                    output.append(GetPosition(row + 1, col - 1))

        if board[position] in black:
            if row == 0:
                board[position] = 24
                return GetPieceLegalMoves(board, position)

            if board[position - 8] == 0:
                output.append(position - 8)

            if col != 7:
                if board[GetPosition(row - 1, col + 1)] in opposition:
                    output.append(GetPosition(row - 1, col + 1))
            if col != 0:
                if board[GetPosition(row - 1, col - 1)] in opposition:
                    output.append(GetPosition(row - 1, col - 1))

        return output

    if board[position] in rook:

        while up <= 7:
            if board[GetPosition(up, col)] != 0:
                if board[GetPosition(up, col)] in opposition:
                    output.append(GetPosition(up, col))
                break
            output.append(GetPosition(up, col))
            up += 1
        while down >= 0:
            if board[GetPosition(down, col)] != 0:
                if board[GetPosition(down, col)] in opposition:
                    output.append(GetPosition(down, col))
                break
            output.append(GetPosition(down, col))
            down -= 1
        while right <= 7:
            if board[GetPosition(row, right)] != 0:
                if board[GetPosition(row, right)] in opposition:
                    output.append(GetPosition(row, right))
                break
            output.append(GetPosition(row, right))
            right += 1
        while left >= 0:
            if board[GetPosition(row, left)] != 0:
                if board[GetPosition(row, left)] in opposition:
                    output.append(GetPosition(row, left))
                break
            output.append(GetPosition(row, left))
            left -= 1

        return output

    if board[position] in bishop:

        while up <= 7:
            if right <= 7:
                if board[GetPosition(up, right)] != 0:
                    if board[GetPosition(up, right)] in opposition:
                        output.append(GetPosition(up, right))
                    break
                output.append(GetPosition(up, right))
            up += 1
            right += 1
            left -= 1

        up = row + 1
        right = col + 1
        left = col - 1
        while up <= 7:
            if left >= 0:
                if board[GetPosition(up, left)] != 0:
                    if board[GetPosition(up, left)] in opposition:
                        output.append(GetPosition(up, left))
                    break
                output.append(GetPosition(up, left))
            up += 1
            right += 1
            left -= 1

        right = col + 1
        left = col - 1
        while down >= 0:
            if right <= 7:
                if board[GetPosition(down, right)] != 0:
                    if board[GetPosition(down, right)] in opposition:
                        output.append(GetPosition(down, right))
                    break
                output.append(GetPosition(down, right))
            down -= 1
            right += 1
            left -= 1

        right = col + 1
        left = col - 1
        down = row - 1
        while down >= 0:
            if left >= 0:
                if board[GetPosition(down, left)] != 0:
                    if board[GetPosition(down, left)] in opposition:
                        output.append(GetPosition(down, left))
                    break
                output.append(GetPosition(down, left))
            down -= 1
            right += 1
            left -= 1

        return output

    if board[position] in king:
        for i, j in [(1, -1,), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]:
            if 0 <= row+i <= 7 and 0 <= col+j <= 7 and (board[GetPosition(row + i, col + j)] == 0 or board[GetPosition(row + i, col + j)] in opposition):
                output.append(GetPosition(row + i, col + j))

    if board[position] in knight:
        for i, j in [(2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]:
             if 0 <= row + i <= 7 and 0 <= col + j <= 7 and (board[GetPosition(row + i, col + j)] == 0 or board[GetPosition(row + i, col + j)] in opposition):
                output.append(GetPosition(row + i, col + j))

    if board[position] in queen:

        temp = board[position]

        board[position] = player[2]
        bishop_moves = GetPieceLegalMoves(board, position)
        board[position] = player[3]
        rook_moves = GetPieceLegalMoves(board, position)
        board[position] = temp

        return bishop_moves + rook_moves

    return output


def IsPositionUnderThreat(board, position):

    if board[position] in white:
        opposition = black
    elif board[position] in black:
        opposition = white
    else:
        return None

    for i in range(len(board)):
        if board[i] in opposition:
            if position in GetPieceLegalMoves(board, i):
                return True

    return False

def test(board, position):
    x = GetPieceLegalMoves(board, position)
    for val in GetPieceLegalMoves(board, position):
        board[val] = "test"

    PrintBoard(board)
    print(x)


board = [0] * 64
board[0] = 10
