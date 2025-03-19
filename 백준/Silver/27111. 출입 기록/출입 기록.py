import sys
input = sys.stdin.readline

n = int(input())

arr = [-1] * 200001
ans = 0
for _ in range(n):
    a,b = map(int, input().split())
    if arr[a] == b: ans += 1
    elif arr[a] == -1 and b == 0: ans += 1
    else: arr[a] = b
        
ans += arr.count(1)
print(ans)