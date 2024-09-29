from heapq import heappush, heappop

def solution(land, height):
    answer = 0
    n = len(land)
    di, dj = [-1,0,1,0], [0,1,0,-1]
    visited = [[False] * n for _ in range(n)]
    
    q = []
    heappush(q, [0,0,0])
    
    while q:
        c, i, j = heappop(q)
        if not visited[i][j]:
            visited[i][j] = True
            answer += c
            
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < n and 0 <= nj < n:
                    temp_c = abs(land[i][j] - land[ni][nj])
                    if temp_c > height: new_c = temp_c
                    else: new_c = 0
                    heappush(q, [new_c, ni, nj])
                    
    return answer