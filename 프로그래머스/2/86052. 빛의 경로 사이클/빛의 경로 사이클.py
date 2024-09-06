def solution(grid):
    answer = []
    direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visit = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    def pathfind(r, c, d):
        count = 0
        while not visit[r][c][d]:
            visit[r][c][d] = 1
            count += 1 
            if grid[r][c] == 'L': d = (d - 1) % 4
            elif grid[r][c] == 'R': d = (d + 1) % 4
            r = (r + direc[d][0]) % len(grid)
            c = (c + direc[d][1]) % len(grid[0])
            
        return count
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for d in range(4):
                if visit[r][c][d]: continue
                answer.append(pathfind(r, c, d))
                
    return sorted(answer)
