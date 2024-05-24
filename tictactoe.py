"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    countX = 0
    countO = 0
    for i in board:
        for j in i:
            if j == X:
                countX += 1
            elif j == O:
                countO += 1

    if countX - countO == 1: return O
    else: return X
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionList = set()
    for indexI, i in enumerate(board):
        for indexJ, j in enumerate(i):
            if j == None:
                actionList.add((indexI, indexJ))

    return actionList
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    i = action[0]
    j = action[1]

    if(i < 0 or i > 2 or j < 0 or j > 2): #if action i, j out of bounds
        raise Exception("Move invalid: Out of Bounds")
    if(board[i][j] == "X" or board[i][j] == "O"): #if there is already an X or O there
        raise Exception("Move invalid: Space already selected")
    if player(board) == X:
        boardCopy[i][j] = X
    else:
        boardCopy[i][j] = O

    return boardCopy
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board: #checking for horizontal
        if i[0] != EMPTY:
            if i[0] == i[1] and i[1] == i[2]:
                return i[0]
    for index, i in enumerate(board[0]): #checking for vertical
        if (i != EMPTY):
            if board[0][index] == board[1][index] and board[1][index] == board[2][index]:
                return board[0][index]
    if(board[1][1] != EMPTY): #Checking both diagonals
        if board[1][1] == board[0][0] and board[1][1] == board[2][2]:
            return board[1][1]
        if board[1][1] == board[0][2] and board[1][1] == board[2][0]:
            return board[1][1]
    
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True
    for i in board:
        for j in i:
            if(j == EMPTY):
                return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

    raise NotImplementedError

def minimax(board):
    if player(board) == X:
        return findTerminals(board, 1)[1]
    else: 
        return findTerminals(board, -1)[1]
    
def findTerminals(board, goal):
    if terminal(board):
        return (utility(board), None)
    
    if (goal == 1):
        maxScore = -2
        for i in actions(board):
            score = findTerminals(result(board, i), -1)[0]
            if score > maxScore:
                maxScore = score
                bestAction = i
        return (maxScore, bestAction)
    else: 
        minScore = 2
        for i in actions(board):
            score = findTerminals(result(board, i), 1)[0]
            if score < minScore:
                minScore = score
                bestAction = i
        return (minScore, bestAction)
