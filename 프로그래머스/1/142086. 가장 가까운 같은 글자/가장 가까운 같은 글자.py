def solution(s):
    answer = []
    for i,v in enumerate(s):
        result = s[0:i].rfind(v)
        if result == -1: answer.append(-1)
        else: answer.append(i - result)
    return answer