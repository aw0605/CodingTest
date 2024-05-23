def solution(k, score):
    result = []
    answer = []
    for v in score:
        result.append(v)
        result.sort(reverse=True)
        if(len(result) > k): result.pop()
        answer.append(result[len(result)-1])
    return answer