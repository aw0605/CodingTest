def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    cA = [0,0,0]
    
    for i,v in enumerate(answers):
        if v == a1[i%5]: cA[0] += 1
        if v == a2[i%8]: cA[1] += 1
        if v == a3[i%10]: cA[2] += 1
    
    for i,v in enumerate(cA):
        if v == max(cA): answer.append(i+1)
    return answer