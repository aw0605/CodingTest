import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()

stack = []
lenB = len(bomb)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-lenB:]) == bomb:
        for _ in range(lenB): stack.pop()
    
print(''.join(stack)) if stack else print("FRULA")