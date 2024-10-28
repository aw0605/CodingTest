import sys
input = sys.stdin.readline

n = int(input())
have = set(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

ans = []

for v in cards:
    if v in have: ans.append('1')
    else: ans.append('0')
        
print(" ".join(ans))