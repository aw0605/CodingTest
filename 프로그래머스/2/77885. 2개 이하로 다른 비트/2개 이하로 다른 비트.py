def solution(numbers):
    answer = []
    for v in numbers:
        answer.append(((v ^ (v+1)) >> 2) + v + 1)
    return answer
