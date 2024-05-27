def solution(N, stages):
    answer = []
    clearArr = [0] * (N + 1)
    player = len(stages)
    
    for v in stages:
        clearArr[v-1] += 1

    for i in range(N):
        if player > 0: 
            fail = clearArr[i] / player
            player -= clearArr[i]
        else: fail = 0
        answer.append([i+1, fail])
        
    return [i for i,v in sorted(answer, key=lambda x: (-x[1], x[0]))]
