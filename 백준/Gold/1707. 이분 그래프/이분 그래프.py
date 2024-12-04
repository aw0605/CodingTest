import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

k = int(input())

def dfs(s, g):
    visited[s] = g
    for i in graph[s]:
        if not visited[i]:
            x = dfs(i, -g)
            if not x: return 0
        elif visited[s] == visited[i]: return 0
    return 1

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i]:
            res = dfs(i, 1)
            if not res: break

    print("YES" if res else "NO")