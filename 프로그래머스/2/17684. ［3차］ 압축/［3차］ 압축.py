def solution(msg):
    answer = []
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictAlpha = {v: i + 1 for i, v in enumerate(alpha)}
    dictAlpha["nextIdx"] = 27
    
    i = 0
    while i < len(msg):
        w = msg[i]
        j = i + 1
        while j <= len(msg) and dictAlpha.get(msg[i:j]) is not None:
            w = msg[i:j]
            j += 1
        answer.append(dictAlpha[w])
        if j <= len(msg):
            dictAlpha[msg[i:j]] = dictAlpha["nextIdx"]
            dictAlpha["nextIdx"] += 1
        i += len(w)
        
    return answer