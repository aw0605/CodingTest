import re

def solution(s):
    result = []
    for v in s.split("},"):
        result.append(re.sub(r"[{}]", "", v).split(","))
    result.sort(key=len)
    
    answer = []
    for i in result:
        for j in i:
            if j not in answer: answer.append(j)
            
    return [int(v) for v in answer]