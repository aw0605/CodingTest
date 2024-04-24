def solution(arr, k):
    answer = []
    for v in arr:
        if len(answer) == k: return answer
        if not v in answer: answer.append(v)
    while (len(answer) < k):
        answer.append(-1)
    return answer