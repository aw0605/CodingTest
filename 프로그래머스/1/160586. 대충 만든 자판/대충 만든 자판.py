def solution(keymap, targets):
    answer = []
    for target in targets:
        totalCount = 0;
        for w in target:
            count = 101;
            contain = 0;
            for key in keymap:
                if w in key:
                    count = min(count, key.index(w)+1)
                    contain = 1
            if not contain: 
                totalCount = -1
                break
            totalCount += count
        answer.append(totalCount)
            
    return answer