def solution(board, h, w):
    answer = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    cur = board[h][w]
    
    for i in range(4):
        ny = h + dh[i]
        nx = w + dw[i]
        if (0 <= ny < len(board)) and (0 <= nx < len(board)):
            if cur == board[ny][nx]: answer += 1
    return answer