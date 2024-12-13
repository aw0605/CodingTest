from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
ans = [0] * (n+1)

q = deque()
q.append(1)

while q:
    cur = q.popleft()
    for v in arr[cur]:
        if not ans[v]:
            ans[v] = cur
            q.append(v)
            
print('\n'.join(map(str, ans[2:])))