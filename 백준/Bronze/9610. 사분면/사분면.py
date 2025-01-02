import sys
input = sys.stdin.readline

n = int(input())
ans = [0,0,0,0,0]
for _ in range(n):
    x,y = map(int, input().split())
    if x == 0 or y == 0: ans[4] += 1
    elif x > 0 and y > 0: ans[0] += 1
    elif x < 0 and y > 0: ans[1] += 1
    elif x < 0 and y < 0: ans[2] += 1
    else: ans[3] += 1
        
for i in range(5):
    if i < 4: print(f"Q{i+1}: {ans[i]}")
    else: print(f"AXIS: {ans[i]}")