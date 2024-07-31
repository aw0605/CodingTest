from itertools import chain

def solution(n):
    [x, y, num] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0: x += 1
            elif i % 3 == 1: y += 1
            else:
                x -= 1
                y -= 1
            board[x][y] = num
            num += 1
            
    return list(chain(*board))