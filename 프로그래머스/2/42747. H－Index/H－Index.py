def solution(citations):
    answer = []
    
    for i in range(len(citations)+1):
        if len(list(filter(lambda x: x >= i, citations))) >= i: answer.append(i)

    return max(answer)