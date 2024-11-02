import sys
datas = sys.stdin.read().splitlines()

for data in datas:
    stack = []
    if data == '.': break

    for v in data:
        if v in '([': stack.append(v)
        elif v == ')':
            if stack and stack[-1] == '(': stack.pop()
            else:
                stack.append(v)
                break
        elif v == ']':
            if stack and stack[-1] == '[': stack.pop()
            else:
                stack.append(v)
                break

    print("yes" if not stack else "no")
