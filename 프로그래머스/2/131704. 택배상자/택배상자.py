def solution(order):
    answer = 0
    storage = []
    
    for i, n in enumerate(order):
        storage.append(i+1)

        while storage and storage[-1] == order[answer]:
            storage.pop()
            answer += 1

    return answer