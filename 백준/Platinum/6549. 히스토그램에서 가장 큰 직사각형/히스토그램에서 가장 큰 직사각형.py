import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0: break

    stack = []
    ans = 0

    for i, h in enumerate(arr):
        if i == 0: continue
        if stack and stack[-1][1] > h:
            while stack:
                stack_i, stack_h = stack.pop()
                w_start = 1
                if stack: w_start = stack[-1][0]+1
                res = (i - w_start) * stack_h
                ans = max(res, ans)
                
                if not stack or stack[-1][1] <= h: break

        if not stack or stack[-1][1] <= h: stack.append((i, h))

    while stack:
        stack_i, stack_h = stack.pop()
        w_start = 1
        if stack: w_start = stack[-1][0]+1
        res = (arr[0]+1 - w_start) * stack_h
        ans = max(res, ans)

    print(ans)