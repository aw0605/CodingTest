def solution(absolutes, signs):
    answer = 0
    signs = [1 if v == True else -1 for v in signs]
    for i in range(0,len(absolutes)):
        answer += absolutes[i] * signs[i] 
        
    return answer