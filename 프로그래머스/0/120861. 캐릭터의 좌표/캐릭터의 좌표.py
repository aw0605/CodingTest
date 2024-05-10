def solution(keyinput, board):
    x,y = 0,0
    xLimit, yLimit = board[0]//2, board[1]//2
    for v in keyinput:
        if v == "left" and x > -xLimit: x -= 1
        elif v == "right" and x < xLimit: x += 1
        elif v == "up" and y < yLimit: y += 1
        elif v == "down" and y > -yLimit: y -= 1
    return [x,y]