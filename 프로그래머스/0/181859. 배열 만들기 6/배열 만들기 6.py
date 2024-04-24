def solution(arr):
    stk = []
    for i, v in enumerate(arr):
        if len(stk) == 0 or v != stk[-1]: stk.append(v)
        else: stk.pop()
    return stk if len(stk) != 0 else [-1]
