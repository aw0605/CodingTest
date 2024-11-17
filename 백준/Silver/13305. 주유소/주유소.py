import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
costs = list(map(int, input().split()))

minC = costs[0]
ans = dist[0] * costs[0]

for i in range(1, n-1):
    if minC > costs[i]: minC = costs[i]
    ans += minC * dist[i]
    
print(ans)