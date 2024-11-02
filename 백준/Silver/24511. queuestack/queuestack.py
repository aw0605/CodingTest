from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
structure = list(map(int, input().split()))
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

ans = deque()

for v in range(n):
    if structure[v] == 0: ans.appendleft(a[v])
        
for i in range(m):
    ans.append(b[i])
    print(ans.popleft(), end=' ')