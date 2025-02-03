import sys
input = sys.stdin.readline
INF = 10**5  

n = int(input())  
ans = [0, INF]
for i in range(n):  
    j, m = map(int, input().split())  
    nl = ((j - 1) // (m + 1) + 1) * 2  
    if ans[1] > nl:
        ans = [i + 1, nl]  

print(ans[0], ans[1])