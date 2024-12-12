from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    dp = [0] * 10001
    
    q = deque()
    q.append([a, ''])
    dp[a] = 1
    
    while q:
        n, cmd = q.popleft()
        if n == b:
            print(cmd)
            break
        
        d = (n * 2) % 10000
        if not dp[d]:
            dp[d] = 1
            q.append([d, cmd + 'D'])
        
        s = (n - 1) % 10000
        if not dp[s]:
            dp[s] = 1
            q.append([s, cmd + 'S'])
        
        l = (n % 1000) * 10 + n // 1000
        if not dp[l]:
            dp[l] = 1
            q.append([l, cmd + 'L'])
        
        r = (n % 10) * 1000 + n // 10
        if not dp[r]:
            dp[r] = 1
            q.append([r, cmd + 'R'])