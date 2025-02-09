import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    a,b = input().strip().split()
    dic[b] = a
    
S = input().strip()
s,e = map(int, input().split())
res = ""
for v in S: res += dic[v]
    
print(res[s-1:e])