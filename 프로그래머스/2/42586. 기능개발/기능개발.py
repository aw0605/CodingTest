def solution(progresses, speeds):
    answer = []
    day = 0
    d = 0
    
    while len(progresses)> 0:
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            d += 1
        else:
            if d > 0:
                answer.append(d)
                d = 0
            day += 1
            
    answer.append(d)
    
    return answer