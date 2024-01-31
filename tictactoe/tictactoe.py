"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xs, os = 0, 0

    for v in board:
        for k in v:
            if k == "X":
                xs += 1
            elif k == "O":
                os += 1

    if xs == os:
        return X
    return O if xs > os else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action

    if type(i) is tuple:
        j = i[1]
        i = i[0]
    if board[i][j] != EMPTY:
        raise Exception("Invalid move")

    clone = copy.deepcopy(board)
    clone[i][j] = player(clone)

    return clone


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == X:
            return X
        elif board[0][col] == board[1][col] == board[2][col] == O:
            return O

    # Check diagonals
    if (
        board[0][0] == board[1][1] == board[2][2] == X
        or board[0][2] == board[1][1] == board[2][0] == X
    ):
        return X
    elif (
        board[0][0] == board[1][1] == board[2][2] == O
        or board[0][2] == board[1][1] == board[2][0] == O
    ):
        return O

    # No winner
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    hasEmpty = False
    for row in board:
        if EMPTY in row:
            hasEmpty = True
    if winner(board) != EMPTY or not hasEmpty:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner_player = winner(board)
    return 1 if winner_player == X else -1 if winner_player == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None, utility(board)  # Return None for best_move when the game is over

    current_player = player(board)
    moves = actions(board)
    if current_player == X:
        best_score = -math.inf
        best_move = None
        for move in moves:
            result_board = result(board, move)
            _, score = minimax(result_board)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move, best_score
    else:
        best_score = float("inf")
        best_move = None
        for move in moves:
            result_board = result(board, move)
            _, score = minimax(result_board)
            if score < best_score:
                best_score = score
                best_move = move
        return best_move, best_score
