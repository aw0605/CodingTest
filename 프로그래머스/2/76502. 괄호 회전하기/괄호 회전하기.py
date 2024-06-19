def solution(s):
    if len(s) % 2: return 0
    answer = 0
    
    for i in range(len(s)):
        stack = []
        rots = s[i:] + s[:i]
        
        for j in rots:   
            if stack and stack[-1] == '[' and j == ']': stack.pop()
            elif stack and stack[-1] == '{' and j == '}': stack.pop()
            elif stack and stack[-1] == '(' and j == ')': stack.pop()
            else: stack.append(j)
        
        if not stack: answer += 1
        
    return answer