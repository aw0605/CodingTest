from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    isTree = True
    while q:
        cur = q.popleft()
        if visited[cur]: isTree = False
        visited[cur] = 1
        for nn in graph[cur]:
            if not visited[nn]: q.append(nn)
    return isTree

case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n + 1)
    count = 0

    for node in range(1, n+1):
        if visited[node]: continue
        if bfs(node): count += 1

    if count == 0: print(f'Case {case}: No trees.')
    elif count == 1: print(f'Case {case}: There is one tree.')
    else: print(f'Case {case}: A forest of {count} trees.')