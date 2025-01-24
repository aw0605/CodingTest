import sys
input = sys.stdin.readline

n = int(input())

cows = [-1] * 10
ans = 0
for _ in range(n):
    c, p = map(int, input().split())
    if cows[c-1] == -1: cows[c-1] = p 
    elif cows[c-1] != p: 
        ans += 1
        cows[c-1] = p
        
print(ans)