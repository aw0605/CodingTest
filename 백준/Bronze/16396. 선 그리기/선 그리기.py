import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * 10001
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x,y):
        ans[i] = 1
        
print(sum(ans))