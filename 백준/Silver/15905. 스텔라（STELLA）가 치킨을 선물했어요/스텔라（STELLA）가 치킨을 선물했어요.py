import sys
input = sys.stdin.readline

n = int(input())
if n == 5: 
    print(0)
    sys.exit()
    
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[0], x[1]))

targetQ, targetP = arr[4]
ans = sum(1 for q,p in arr if q == targetQ and p > targetP)
print(ans)