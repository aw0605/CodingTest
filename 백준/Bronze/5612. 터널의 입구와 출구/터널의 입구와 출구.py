import sys
input = sys.stdin.readline

n,m = int(input()), int(input())
ans = m
for _ in range(n):
    i,o = map(int, input().split())
    m += i - o
    if m < 0: 
        print(0)
        exit()
    ans = max(ans,m)
    
print(ans)    