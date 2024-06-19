def solution(s):
    if len(s) % 2: return 0

    answer = 0
    pair = { ")": "(", "}": "{", "]": "[" }
    
    for i in range(len(s)):
        stack = []
        rotS = s[i:] + s[:i]
        
        for j in rotS:
            if j in pair and stack and stack[-1] == pair[j]: stack.pop()
            else: stack.append(j)

        if not stack: answer += 1
        
    return answer
