def solution(board):
    def isValid(x,y): return 0 <= x < N and 0 <= y < N
    
    def isBlock(x,y): return (x,y) == (0,0) or not isValid(x,y) or board[x][y] == 1

    def calcCost(direction, prev_direction, cost):
        if prev_direction == -1 or (prev_direction - direction) % 2 == 0:
            return cost + 100
        else: return cost + 600
    
    def isUpdate(x, y, direction, new_cost):
        return visited[x][y][direction] == 0 or visited[x][y][direction] > new_cost
    
    q = [(0,0,-1,0)]
    N = len(board)
    directions = [(0,-1),(-1,0),(0,1),(1,0)]
    visited = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    answer = float("inf")
    
    while q:
        x,y,prev_direction,cost = q.pop(0)
        for direction, (dx,dy) in enumerate(directions):
            nx,ny = x + dx, y + dy
            if isBlock(nx,ny): continue
            new_cost = calcCost(direction, prev_direction, cost)
            if (nx, ny) == (N-1, N-1): answer = min(answer, new_cost)
            elif isUpdate(nx, ny, direction, new_cost):
                q.append((nx, ny, direction, new_cost))
                visited[nx][ny][direction] = new_cost
                
    return answer