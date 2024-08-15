from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[0]*M for _ in range(N)]

    answer = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]=='X' or visited[i][j]:
                continue
            queue = deque()
            queue.append((i,j))
            visited[i][j]=1
            n_food = int(maps[i][j])
            while queue:
                i0, j0 = queue.popleft()
                for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni, nj = i0+di, j0+dj
                    if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and maps[ni][nj]!='X':
                        queue.append((ni,nj))
                        visited[ni][nj] = 1
                        n_food += int(maps[ni][nj])
            answer.append(n_food)
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer