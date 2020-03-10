from MoveGen import *
count = 0
MAX_LEVEL =4

values = {10: 1, 20: 1, 11: 3, 21: 3, 12: 3, 22: 3, 13: 5, 23: 5, 14: 9, 24: 9, 15: 6969, 25: 6969}


black_pawn = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
              5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
              1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
              0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
              0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
              0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
              0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
              0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]

white_pawn =  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
               0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
               0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
               0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
               0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
               1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
               5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

all_knight = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
          -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
          -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
          -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
          -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
          -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
          -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
          -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]

black_bishop = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
         -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
         -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
         -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
         -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
         -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
         -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
         -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

white_bishop = [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
                -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
                -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
                -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
                -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
                -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
                -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
                -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

black_rook = [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
          0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
          0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]

white_rook = [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0,
              -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
              -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
              -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
              -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
              -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
              0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
              0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

black_queen = [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
         -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
         -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
         -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
          0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
         -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
         -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
         -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

white_queen = [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
               -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
               -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
               0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
               -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
               -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
               -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
               -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

black_king = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                 -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                 -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                 -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                 -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
                 -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
                  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
                  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]

white_king = [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0,
              2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
              -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
              -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
              -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
              -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
              -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
              -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0]


def PositionValue(board, position):
    if board[position] in knight:
        return all_knight[position]
    if board[position] in white:
        if board[position] in pawn:
            return white_pawn[position]
        elif board[position] in rook:
            return white_rook[position]
        elif board[position] in bishop:
            return white_bishop[position]
        elif board[position] in queen:
            return white_queen[position]
        elif board[position] in king:
            return white_king[position]
    elif board[position] in black:
        if board[position] in pawn:
            return black_pawn[position]
        elif board[position] in rook:
            return black_rook[position]
        elif board[position] in bishop:
            return black_bishop[position]
        elif board[position] in queen:
            return black_queen[position]
        elif board[position] in king:
            return black_king[position]


def BoardValue(board, player):

    score = 0

    for pos in range(len(board)):
        if board[pos] == 0:
            continue
        elif board[pos] in player:
            score += values[board[pos]] + (PositionValue(board, pos) / 10)
        else:
            score -= values[board[pos]] + (PositionValue(board, pos) / 10)

    return score


def SmartBoardValue(board, player, score, move):

    new_score = score
    opposition = white if player == black else black

    old_position = PositionValue(board, move[0])
    new_board = makeMoveCopy(board, move[0], move[1])
    if move[1] in opposition:
        new_score += values[new_board[move[1]]]
    new_position = PositionValue(new_board, move[1])

    score += (new_position - old_position)

    return score


def SortMoves(moves):

    move = list(moves)
    sorted_list = []
    for i in range(len(move)):
        for j in range(0, len(move) - i - 1):
            if move[j][1] > move[j+1][1]:
                move[j], move[j+1] = move[j+1], move[j]

    for i in range(len(move)):
        del move[i][1]
        sorted_list.append(move[i][0])

    return sorted_list


def MoveValues(board, player):
    moveValList = []

    for move in AllMoves(board, player):
        new_board = makeMoveCopy(board, move[0], move[1])
        moveValList.append([move, BoardValue(new_board, player)])

    return moveValList

"""
def minimax(board, player, alpha = -99999999, beta = 999999999, level = 0, max_level = MAX_LEVEL):

    global count

    if level == max_level:
        if level % 2 == 0:
            bigPlayer = player
        else:
            bigPlayer = black if player == white else white
        count += 1
        return None, BoardValue(board, bigPlayer)

    bestScore = -9999999 if level%2 == 0 else 9999999

    for move in AllMoves(board, player):
        new_board = makeMoveCopy(board, move[0], move[1])
        downMove, score = minimax(new_board, black if player == white else white, alpha, beta, level + 1)
        if level % 2 == 0:
            if score > bestScore:
                bestScore = score
                bestMove = move
                alpha = max(alpha, bestScore)
                if alpha >= beta:
                    break

        else:
            if score < bestScore:
                bestScore = score
                bestMove = move
                beta = min(beta, bestScore)
                if alpha >= beta:
                    break
    return bestMove, bestScore
"""

def minimax(board, player, alpha = -99999999, beta = 999999999, level = 0, max_level = MAX_LEVEL, currentBoardVal=None):

    global count

    if level == max_level:
        count += 1
        return None, currentBoardVal

    if currentBoardVal is None:
        currentBoardVal = BoardValue(board, player)

    bestScore = -9999999 if level%2 == 0 else 9999999

    for move in AllMoves(board, player):

        newBoardVal = SmartBoardValue(board, player, currentBoardVal, move)
        new_board = makeMoveCopy(board, move[0], move[1])

        downMove, score = minimax(new_board, black if player == white else white, alpha, beta, level + 1, currentBoardVal=newBoardVal)
        if level % 2 == 0:
            if score > bestScore:
                bestScore = score
                bestMove = move
                alpha = max(alpha, bestScore)
                if alpha >= beta:
                    break

        else:
            if score < bestScore:
                bestScore = score
                bestMove = move
                beta = min(beta, bestScore)
                if alpha >= beta:
                    break
    return bestMove, bestScore


def IsPositionUnderThreat(board, pos):

    opponent = white if board[pos] in black else black
    opponent_moves = []

    for opponent_pos in range(len(board)):
        if board[opponent_pos] in opponent:
            for move in GetPieceLegalMoves(board, opponent_pos):
                opponent_moves.append(move)

    if pos in opponent_moves:
        return True
    else:
        return False


def CheckMate(board, player):

    status = False

    king_pos = None
    for pos in range(len(board)):
        if board[pos] == player[5]:
            king_pos = pos

    if IsPositionUnderThreat(board, king_pos):
        status = True
        for move in GetPieceLegalMoves(board, king_pos):
            new_board = makeMove(board, king_pos, move)
            if not IsPositionUnderThreat(new_board, move):
                status = False
                break

    return status





