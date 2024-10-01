def solution(keyinput, board):
    x,y = 0,0
    moves = {"up": [0,1], "down": [0,-1], "left": [-1,0], "right": [1,0]}
    w,h = board[0]//2, board[1]//2
    
    def isValid(x,y, dx,dy):
        return -w <= x+dx <= w and -h <= y+dy <= h
    
    for k in keyinput:
        dx,dy = moves[k]
        if isValid(x,y, dx,dy):
            x += dx
            y += dy
            
    return [x,y]