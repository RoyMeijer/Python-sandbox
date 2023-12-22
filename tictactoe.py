"""
Tic Tac Toe Player
"""
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countEmpty = sum(cell == EMPTY for row in board for cell in row)
    turnOfPlayer = X if (countEmpty % 2) == 1 else O
    return turnOfPlayer


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                all_actions.add((i, j))

    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)
    board2[action[0]][action[1]] = player(board)

    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    for column in zip(*board):
        if len(set(column)) == 1:
            return column[0]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    action_list = list()
    if player(board) == X:
        for action in actions(board):
            action_list.append((min_value(result(board, action)), action))
        return max(action_list)[1]
    if player(board) == O:
        for action in actions(board):
            action_list.append((max_value(result(board, action)), action))
        return min(action_list)[1]


def min_value(board):
    if terminal(board):
        return utility(board)
    return min(max_value(result(board, action)) for action in actions(board))


def max_value(board):
    if terminal(board):
        return utility(board)
    return max(min_value(result(board, action)) for action in actions(board))
