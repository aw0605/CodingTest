def solution(keymap, targets):  
    answer = []
    keys = {}
    for key in keymap:
        for i,v in enumerate(key):
            keys[v] = min(keys[v], i + 1) if v in keys else i + 1
            
    for i,target in enumerate(targets):
        total = 0
        for w in target:
            if w not in keys: 
                total = -1
                break
            total += keys[w]
        answer.append(total)
        
    return answer