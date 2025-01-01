import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
score = 1
for v in arr:
    if v:
        ans += score
        score += 1
    else: 
        score = 1
        
print(ans)