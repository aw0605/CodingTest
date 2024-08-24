def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        sentence = ""
        idx = 0

        while idx < len(s):
            cnt = 1
            while s[idx:idx+i] == s[idx+i:idx+i+i]:
                cnt += 1
                idx += i
            
            if cnt > 1:
                sentence += str(cnt)
            sentence += s[idx:idx+i]
            idx += i
        
        answer = min(answer, len(sentence))
    
    return answer
