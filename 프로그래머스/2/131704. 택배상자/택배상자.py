def solution(order):
    answer = 0
    stacks = []
    i = 1
    
    while i < len(order)+1:
        stacks.append(i)
        while stacks[-1] == order[answer]:
            answer += 1
            stacks.pop()
            if len(stacks) == 0: break
        i += 1

    return answer