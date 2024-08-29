def get_count(board, kind):
    return sum(row.count(kind) for row in board)

def check_win(board, kind):
    win_lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]

    return any(all(cell == kind for cell in line) for line in win_lines)

def is_board_valid(board):
    o_count = get_count(board, "O")
    x_count = get_count(board, "X")

    if x_count > o_count or o_count > x_count + 1: return False
    if check_win(board, "O") and o_count != x_count + 1: return False
    if check_win(board, "X") and x_count != o_count: return False

    return True

def solution(board):
    return 1 if is_board_valid(board) else 0
