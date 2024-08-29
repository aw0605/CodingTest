def check_tic_tac_toe(board, sign):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    
    for a, b, c in lines:
        if board[a] == sign and board[b] == sign and board[c] == sign: return True
    return False

def solution(board):
    board = [val for row in board for val in row]
    O = board.count('O')
    X = board.count('X')

    if O < X or O - X > 1: return 0

    o_wins = check_tic_tac_toe(board, 'O')
    x_wins = check_tic_tac_toe(board, 'X')

    if o_wins and x_wins: return 0
    if o_wins and O - X != 1: return 0
    if x_wins and O != X: return 0

    return 1
