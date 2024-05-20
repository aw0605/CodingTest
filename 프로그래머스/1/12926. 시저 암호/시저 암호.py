def solution(s, n):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    answer = ""
    
    for v in s:
        if v != " ":
            idx = alpha.index(v.casefold())+n
            if idx > len(alpha)-1: idx %= len(alpha)
        
        if v == " ": answer += v
        elif v in alpha: answer += alpha[idx]
        else: answer += alpha[idx].upper()
        
    return answer