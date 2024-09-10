def solution(s):
    stack = []
    
    for v in s:
        if stack and stack[-1] == v: stack.pop()
        else: stack.append(v)

    return int(not stack)