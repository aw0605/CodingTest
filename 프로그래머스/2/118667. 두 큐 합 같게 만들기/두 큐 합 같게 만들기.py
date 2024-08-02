from collections import deque

def solution(queue1, queue2):
    answer = 0
    mid = (sum(queue1) + sum(queue2)) // 2
    sum1 = sum(queue1)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while queue1 and queue2:
        if sum1 > mid:
            cur = queue1.popleft()
            sum1 -= cur

        elif sum1 < mid:
            cur = queue2.popleft()
            sum1 += cur
            queue1.append(cur)
        else: return answer
        answer += 1

    return -1