def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s = sorted(s, key = len)
    
    for v in s:
        numbers = v.split(",")
        for n in numbers:
            if int(n) not in answer: answer.append(int(n))
            
    return answer