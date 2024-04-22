def solution(strArr):
    answer = []
    for i,v in enumerate(strArr):
        if i % 2 != 0: answer.append(v.upper())
        else: answer.append(v.lower())
    return answer