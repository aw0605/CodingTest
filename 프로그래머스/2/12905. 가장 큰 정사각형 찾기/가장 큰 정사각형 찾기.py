def solution(board):
    r,c = len(board), len(board[0])
    
    for i in range(1,r):
        for j in range(1,c):
            if board[i][j] == 1:
                up, left, up_left = (
                    board[i-1][j],
                    board[i][j-1],
                    board[i-1][j-1]
                )
                
                board[i][j] = min(up, left, up_left) + 1

    return max(max(r) for r in board) ** 2