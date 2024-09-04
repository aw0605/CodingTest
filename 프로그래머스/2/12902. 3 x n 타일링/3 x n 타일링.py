def solution(n):
    if n % 2 == 1: return 0

    a = 1
    answer = 1
    total = 0
    i = 2
    
    while i <= n:
        answer = a*3 + total*2
        total += a
        a = answer
        i += 2
        
    return answer % 1000000007