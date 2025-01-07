import sys
input = sys.stdin.readline

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def noneSum(S):    
    ans = 0
    for v in alpha:
        if v not in S: ans += ord(v)
    return ans

n = int(input())
for _ in range(n):
    S = input().strip()
    print(noneSum(S))