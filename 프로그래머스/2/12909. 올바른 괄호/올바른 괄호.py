def solution(s):
    stack = []
    
    for v in s:
        if len(stack) == 0: stack.append(v)
        elif stack[-1] == "(" and v == ")": stack.pop()
        else: stack.append(v)

    return False if len(stack) else True