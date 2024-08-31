import math

def check(num):
    check_arr = []
    if num == 1: return 0

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            check_arr.append(i)
            if num // i <= 10**7: return num // i
    
    if len(check_arr) != 0: return check_arr[-1]
    return 1

def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        check_num = check(i)
        if check_num is not None: answer.append(check_num)
    
    return answer
