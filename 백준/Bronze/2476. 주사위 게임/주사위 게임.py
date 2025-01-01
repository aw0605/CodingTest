import sys
input = sys.stdin.readline

n = int(input())

ans = 0
for _ in range(n):
    dice = [0,0,0,0,0,0,0]
    a,b,c = map(int, input().split())
    dice[a] += 1
    dice[b] += 1
    dice[c] += 1
    same = max(dice)
    score = 0
    
    if same == 3: score = 10000 + (dice.index(same) * 1000)
    elif same == 2: score = 1000 + (dice.index(same) * 100)
    else: score = max(a,b,c) * 100
        
    ans = max(ans, score)
    
print(ans)