def isValid(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

def nextLoc(x, y, direc):
    if direc == "U": nx, ny = x, y + 1
    elif direc == "D": nx, ny = x, y - 1
    elif direc == "L": nx, ny = x + 1, y
    elif direc == "R": nx, ny = x - 1, y
    return nx, ny

def solution(dirs):
    answer = set()
    x,y = 5,5
    
    for direc in dirs:
        nx, ny = nextLoc(x, y, direc)
        if not isValid(nx, ny): continue
        answer.add((x,y,nx,ny))
        answer.add((nx,ny,x,y))
        x, y = nx, ny
        
    return len(answer) / 2