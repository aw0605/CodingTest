def solution(array, n):
    array.sort()
    answer = []
    for v in array:
        answer.append(abs(n - v))
    return array[answer.index(min(answer))]