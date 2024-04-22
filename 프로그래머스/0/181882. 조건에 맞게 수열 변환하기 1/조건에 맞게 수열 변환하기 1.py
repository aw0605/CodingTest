def solution(arr):
    answer = []
    for v in arr:
        if v % 2 == 0 and v >= 50: answer.append(v / 2)
        elif v % 2 != 0 and v <= 50: answer.append(v * 2)
        else: answer.append(v)
    return answer