import sys
input = sys.stdin.readline

n,m = map(int, input().split())
s1 = [input().strip() for _ in range(n)]
s2 = [input().strip() for _ in range(n)]
    
s = []
for i in range(n):
    res = ""
    for v in s1[i]:
        res += v * 2
    s.append(res)
    
print("Eyfa" if s == s2 else "Not Eyfa")