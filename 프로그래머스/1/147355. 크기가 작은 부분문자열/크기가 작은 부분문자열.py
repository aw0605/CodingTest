def solution(t, p):
    answer = []
    for i in range(0,len(t) - len(p)+1):
        num = int(t[i:i+len(p)])
        if num <= int(p): answer.append(num)
    return len(answer)