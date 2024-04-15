def solution(intStrs, k, s, l):
    result = ""
    answer = []
    for str in intStrs:
        result = int(str[s:s+l])
        if result > k:
            answer.append(result)
    return answer