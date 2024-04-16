def solution(start, end_num):
    answer = []
    for i in range(end_num, start+1):
        answer.append(i)
    return answer[::-1]