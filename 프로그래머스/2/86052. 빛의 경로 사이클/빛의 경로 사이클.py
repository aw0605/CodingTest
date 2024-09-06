def solution(grid):
    answer = []
    dy = (1, 0, -1, 0)
    dx = (0, -1, 0, 1)
    yl, xl = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(xl)] for _ in range(yl)]

    for y in range(yl):
        for x in range(xl):
            for d in range(4):
                if visited[y][x][d]: continue
                count = 0
                ny, nx = y, x
                
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == "L": d = (d - 1) % 4
                    elif grid[ny][nx] == "R": d = (d + 1) % 4

                    ny = (ny + dy[d]) % yl 
                    nx = (nx + dx[d]) % xl
                
                answer.append(count)

    return sorted(answer)
