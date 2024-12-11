import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dist(a, b):
    return abs(inc[a][0] - inc[b][0]) + abs(inc[a][1] - inc[b][1])

def sol(a, b):
    next = max(a, b) + 1
    if next == w + 2: return 0
    if dp[a][b] != -1: return dp[a][b]

    a_dist = sol(next, b) + dist(a, next)
    b_dist = sol(a, next) + dist(b, next)

    if a_dist < b_dist:
        dp[a][b] = a_dist
        trace[a][b] = 1
    else:
        dp[a][b] = b_dist
        trace[a][b] = 2

    return dp[a][b]

n = int(input())
w = int(input())

inc = [[1, 1], [n, n]]
for _ in range(w):
    i, j = map(int, input().split())
    inc.append([i, j])

dp = [[-1] * 1002 for _ in range(1002)]
trace = [[-1] * 1002 for _ in range(1002)]

print(sol(0, 1))

a, b = 0, 1
for i in range(2, w + 2):
    print(trace[a][b])
    if trace[a][b] == 1: a = i
    else: b = i