import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ops = input().strip()
    stack = 0
    
    for v in ops:
        if v == "(": stack += 1
        elif v == ")":
            if not stack:
                stack += 1
                break
            else:
                stack -= 1
    
    if stack: print("NO")
    else: print("YES")
            
    