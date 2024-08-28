def solution(r1, r2):
    answer = 0
    
    for i in range(1,r2):
        num2 = int((r2**2-i**2)**0.5)
        if i >= r1: answer += 4*(num2+1)
        else:
            num1 = int((r1**2-i**2)**0.5)
            if num1**2+i**2 == r1**2: answer+=4*(num2-num1+1)
            else: answer+=4*(num2-num1)

    return answer + 4