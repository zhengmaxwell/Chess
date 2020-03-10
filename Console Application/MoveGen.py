from board import *


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


def AllMoves(board, player):

    output = []
    for pos in range(len(board)):
        if board[pos] in player:
            for new_pos in GetPieceLegalMoves(board, pos):
                output.append([pos, new_pos])

    return output


def makeMoveCopy(board, pos, new_pos):
    new_board = list(board)
    return makeMove(new_board, pos, new_pos)


def makeMove(board, pos, new_pos):

    val = board[pos]
    board[pos] = 0
    board[new_pos] = val

    return board












