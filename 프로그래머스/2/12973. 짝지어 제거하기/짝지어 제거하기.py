def solution(s):
    stack = []
    
    for v in s:
        if not len(stack): stack.append(v)
        elif stack[-1] == v: stack.pop()
        else: stack.append(v)

    return 0 if len(stack) else 1