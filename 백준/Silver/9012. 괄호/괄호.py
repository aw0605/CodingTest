import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t): 
    stack = 0
    ops = input().strip()
    if ops[0] == ')' or ops[-1] == '(':
        print('NO')
        continue
    for v in ops:
        if v == '(': 
            stack += 1
        elif v == ')':
            if not stack:
                print('NO')
                break
            else: stack -= 1
    else:
        if not stack: print('YES')
        else: print('NO')