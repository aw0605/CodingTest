import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
values = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)
    
dp = [[0, 0] for _ in range(n+1)]
num = [[[], []] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(cur):
    visited[cur] = 1
    dp[cur][0] = values[cur]
    num[cur][0].append(cur)
    for nn in tree[cur]:
        if not visited[nn]:
            dfs(nn)
            dp[cur][0] += dp[nn][1]
            for i in num[nn][1]: num[cur][0].append(i)
            if dp[nn][0] <= dp[nn][1]: 
                dp[cur][1] += dp[nn][1]
                for i in num[nn][1]:
                    num[cur][1].append(i)
            else:
                dp[cur][1] += dp[nn][0]
                for i in num[nn][0]:
                    num[cur][1].append(i)

dfs(1)

if dp[1][0] >= dp[1][1]: i = 0
else: i = 1

print(dp[1][i])

ans = num[1][i]
ans.sort()
print(*ans)