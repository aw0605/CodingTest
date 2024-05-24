def solution(number, limit, power):
    answer = 1
    
    for k in range(2,number+1):
        gcdN = 0
        for i in range(1,int(k**0.5)+1):
            if k % i == 0: 
                gcdN += 1
                if i != k//i: gcdN += 1
        answer += gcdN if gcdN <= limit else power
        
    return answer