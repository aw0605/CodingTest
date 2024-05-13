def solution(i, j, k):
    answer = ""
    for v in range(i,j+1): answer += str(v)
    return len(answer.split(str(k))) - 1