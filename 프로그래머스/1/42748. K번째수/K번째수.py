def solution(array, commands):
    answer = []
    for v in commands:
        i,j,k = v
        answer.append(sorted(array[i-1:j])[k-1])
    return answer