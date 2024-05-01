def solution(num_list):
    answer = [0,0]
    for v in num_list:
        answer[v%2] += 1
    return answer
        