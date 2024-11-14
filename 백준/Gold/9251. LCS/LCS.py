import sys
input = sys.stdin.readline

s1, s2 = input().strip(), input().strip()
n, m = len(s1), len(s2)

dp = [0] * m

for i in range(n):
    cur = 0
    for j in range(m):
        if cur < dp[j]: cur = dp[j]
        elif s1[i] == s2[j]: dp[j] = cur + 1

print(max(dp))