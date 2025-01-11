import sys
input = sys.stdin.readline

g = [1,2,3,3,4,10]
s = [1,2,2,2,3,5,10]

t = int(input())
for i in range(1,t+1):
    gArr = list(map(int, input().split()))
    sArr = list(map(int, input().split()))
    gScore = sScore = 0
    for j in range(6):
        gScore += g[j] * gArr[j]
    for j in range(7):
        sScore += s[j] * sArr[j]
    if gScore > sScore: print(f"Battle {i}: Good triumphs over Evil")
    elif gScore < sScore: print(f"Battle {i}: Evil eradicates all trace of Good")
    else: print(f"Battle {i}: No victor on this battle field")