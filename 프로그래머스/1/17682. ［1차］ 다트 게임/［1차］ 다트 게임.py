def solution(dartResult):
    score = ""
    answer = []
    SDTObj = {"S": 1,"D": 2,"T": 3}
    
    for v in dartResult:
        if v.isdigit(): score += v
        elif v.isalpha(): 
            answer.append(int(score) ** SDTObj[v])
            score = ""
        elif v == "*":
            if len(answer) > 1: answer[-2] *= 2
            answer[-1] *= 2
        elif v == "#": answer[-1] *= -1
    
    return sum(answer)