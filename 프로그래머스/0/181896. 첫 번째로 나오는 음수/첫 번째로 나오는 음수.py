def solution(num_list):
    answer = []
    for i, num in enumerate(num_list):
        if num < 0:
            answer.append(i)
            return answer[0]
    return -1