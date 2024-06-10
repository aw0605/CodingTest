dx = {'N':-1, 'S':1, 'E':0, 'W': 0}
dy = {'N': 0, 'S':0, 'E':1, 'W':-1}

def solution(park, routes):
    answer = []
    x, y = -1, -1
    for i, j in enumerate(park):
        if "S" in j: x, y = i, j.index("S") 

    for route in routes:
        direc, dist = route.split(' ')
        isFalse = False
        
        for i in range(1, int(dist) + 1):
            nx, ny = x + dx[direc] * i, y + dy[direc] * i
            if nx < 0 or ny < 0 or nx > len(park)-1 or ny > len(park[0])-1 or park[nx][ny] == 'X':
                isFalse = True
                break

        if isFalse: continue
        nx, ny = x + dx[direc] * int(dist), y + dy[direc] * int(dist)
        x, y = nx, ny

    answer = [x, y]

    return answer

