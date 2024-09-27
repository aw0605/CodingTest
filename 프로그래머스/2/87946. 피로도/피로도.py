def dfs(cur, cnt, dungeons, visited):
    answer = cnt
    for i in range(len(dungeons)):
        if cur >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            answer = max(answer, dfs(cur - dungeons[i][1], cnt+1, dungeons, visited))
            visited[i] = 0
    return answer

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    answer = dfs(k,0,dungeons, visited)
    return answer