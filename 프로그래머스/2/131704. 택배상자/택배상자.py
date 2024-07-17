def solution(order):
    answer = 0
    storage = []
    j = 0
    for i in range(1, len(order) + 1):
        storage.append(i)
        while storage and (storage[-1] == order[j]):
            answer += 1
            j += 1
            storage.pop()

    return answer