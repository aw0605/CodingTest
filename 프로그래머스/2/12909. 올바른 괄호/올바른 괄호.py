def solution(s):
    stack = []
    
    for v in s:
        if v == '(': stack.append(v)

        if v == ')':
            try: stack.pop()
            except IndexError: return False

    return len(stack) == 0