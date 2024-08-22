def solution(board):
    board_T = [list(x) for x in zip(*board)]
    side = max(max(board[0]), max(board_T[0]))

    n = len(board)
    m = len(board[0])

    for i in range(1, m):
        for j in range(1, n):
            if board[j][i] == 1:
                board[j][i] += min(board[j-1][i],board[j][i-1],board[j-1][i-1])
                if side < board[j][i]: side = board[j][i]
                       
    return side**2