def getCollatz(k):
    result = []
    
    while k != 1:
        result.append(k)
        k = k / 2 if k % 2 == 0 else k * 3 + 1     
    result.append(k)
    
    return result
 
def solution(k, ranges):
    answer = []
    collatz = getCollatz(k)

    for r in ranges:
        total = 0
        ubakRange = collatz[r[0] : len(collatz)+r[1]]
        
        if r[0] >= r[1] + len(collatz):
            answer.append(-1)
            continue
            
        for i in range(len(ubakRange) - 1):
            total += (((ubakRange[i] + ubakRange[i+1]) * 1) / 2)
            
        answer.append(total)
        
    return answer