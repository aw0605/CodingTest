def solution(msg):
    answer = []
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictAlpha = {v:i+1 for i,v in enumerate(alpha)}
    
    while True:
        if msg in dictAlpha:
            answer.append(dictAlpha[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in dictAlpha:
                answer.append(dictAlpha[msg[0:i-1]])
                dictAlpha[msg[0:i]] = len(dictAlpha)+1
                msg = msg[i-1:]
                break

    return answer