def solution(dirs):
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()
    x, y = 0, 0
    
    for v in dirs:
        nx, ny = x + moves[v][0], y + moves[v][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x, y = nx, ny

    return len(visited)//2