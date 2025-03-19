import sys
input = sys.stdin.readline

n = int(input())

arr = set()
ans = 0
for _ in range(n):
    a,b = map(int, input().split())
    if b == 1:
        if a in arr: ans += 1
        else: arr.add(a)
    else:
        if a not in arr: ans += 1
        else: arr.remove(a)
        
ans += len(arr)
print(ans)