"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    if board == initial_state():
    	return X

    sum_x = 0
    sum_O = 0
    for row in board:
    	sum_x += row.count(X)
    	sum_O += row.count(O)

    if sum_x > sum_O:
    	return O
    else:
    	return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == EMPTY:
    			possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
    	raise Exception("Invalid move")

    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board

   


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    scores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
    	for j in range(3):
    		if board[i][j] == X:
    			scores[i][j] += 1
    		elif board[i][j] == O:
    			scores[i][j] += -1
    		else:
    			continue

    sum_row = [sum(x) for x in scores]
    sum_column = [sum(x) for x in zip(*scores)]
    sum_cross = sum([scores[i][i] for i in range(3)])
    sum_back_cross = sum([scores[i][2-i] for i in range(3)])

    all_scores = sum_row + sum_column + [sum_cross] + [sum_back_cross]

    for score in all_scores:
    	if score == 3:
    		return X
    	elif score == -3:
    		return O

    return None

   


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
    	return True

    count = 0
    for i in range(3):
    	for j in range(3):
    		if board[i][j] is not EMPTY:
    			count += 1

    return True if count == 9 else False    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
    	if winner(board) == X:
    		return 1
    	elif winner(board) == O:
    		return -1
    	else:
    		return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
    	return None
    else:
    	if player(board) == X:
    		value, move = max_value(board)
    		return move
    	else:
    		value, move = min_value(board)
    		return move

    

def max_value(board):
	if terminal(board):
		return utility(board), None

	v = float('-inf')
	move = None
	for action in actions(board):
		aux, act = min_value(result(board, action))
		if aux > v:
			v = aux
			move = action
			if v == 1:
				return v, move

	return v, move




def min_value(board):
	if terminal(board):
		return utility(board), None

	v = float('inf')
	move = None
	for action in actions(board):
		aux, act = max_value(result(board, action))
		if aux < v:
			v = aux
			move = action
			if v == -1:
				return v, move

	return v, move


"""
board = [[X, EMPTY, O],
            [EMPTY, O, EMPTY],
            [X, EMPTY, EMPTY]]
#print(actions(board))

for action in actions(board):
	print(min_value(board))
"""