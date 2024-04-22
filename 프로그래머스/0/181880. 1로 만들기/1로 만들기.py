def solution(num_list):
    answer = 0
    for v in num_list:
        while v != 1:
            if v % 2 == 0: v = v // 2
            else: v = (v - 1) // 2
            answer += 1
    return answer