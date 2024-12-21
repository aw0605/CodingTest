import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
tree = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int , input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0,0] for i in range(n+1)]
visited = [0] * (n+1)

def dfs(s):
    visited[s] = 1
    if len(tree[s]) == 0:
        dp[s][1] = 1
        dp[s][0] = 0
    else:
        for i in tree[s]:
            if not visited[i]:
                dfs(i)
                dp[s][0] += dp[i][1]
                dp[s][1] += min(dp[i][0] , dp[i][1])
        dp[s][1] += 1

dfs(1)

print(min(dp[1][0],dp[1][1]))