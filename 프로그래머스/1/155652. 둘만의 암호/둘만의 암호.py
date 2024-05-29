def solution(s, skip, index):
    answer = ''

    for w in s:
        i = 0;
        while i < index:
            w = chr((ord(w) - ord('a') + 1) % 26 + ord('a'))
            if w not in skip: i += 1
        answer += w
            
    return answer