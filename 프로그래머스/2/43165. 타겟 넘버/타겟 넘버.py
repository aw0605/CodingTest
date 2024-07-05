def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1 * numbers[0],0]]
    n = len(numbers)

    while queue:
        cur, i = queue.pop()
        i += 1
        if i < n:
            queue.append([cur+numbers[i], i])
            queue.append([cur-numbers[i], i])
        else:
            if cur == target: answer += 1
            
    return answer