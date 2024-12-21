from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
cost = [0] + [int(x) for x in input().split()]
tree = defaultdict(list)
for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(cur):
    visited[cur] = 1
    for v in tree[cur]:
        if not visited[v]:
            dfs(v)
            dp[cur][0] += max(dp[v][0], dp[v][1])
            dp[cur][1] += dp[v][0]

dp = [[0, cost[i]] * 2 for i in range(n+1)]
visited = [0] * (n+1)

dfs(1)

print(max(dp[1][1], dp[1][0]))