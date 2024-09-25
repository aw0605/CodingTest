def dfs(computers, visited, node):
    visited[node] = True
    for i,c in enumerate(computers[node]):
        if c and not visited[i]: dfs(computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
            
    return answer