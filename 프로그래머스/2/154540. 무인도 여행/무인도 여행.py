import sys
    
def solution(maps):
    sys.setrecursionlimit(int(1e9))

    graph = [list(row) for row in maps]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    ans = []

    def dfs(x, y):
        cnt = 0
        if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
            return cnt
        if not graph[x][y].isdigit():
            return cnt
        cnt = int(graph[x][y])
        graph[x][y] = 'X'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cnt += dfs(nx, ny)
        return cnt

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j].isdigit():
                ans.append(dfs(i,j))

    return sorted(ans) if len(ans) != 0 else [-1]