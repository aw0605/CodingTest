def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        stack = []
        for j in range(n):
            cur = s[(i+j) % n]
            if cur == "(" or cur == "[" or cur == "{": stack.append(cur)
            else:
                if not stack: break
        
                if cur == ")" and stack[-1] == "(": stack.pop()
                elif cur == "]" and stack[-1] == "[": stack.pop()
                elif cur == "}" and stack[-1] == "{": stack.pop()
                else: break
        else:
            if not stack: answer += 1
        
    return answer