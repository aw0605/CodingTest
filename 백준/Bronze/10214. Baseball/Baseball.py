import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    yS, kS = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        yS += y
        kS += k
    
    if yS > kS: print("Yonsei")
    elif yS < kS: print("Korea")
    else: print("Draw")