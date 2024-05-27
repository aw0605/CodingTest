def solution(N, stages):
    answer = []
    clearArr = [0] * (N + 1)
    
    for v in stages:
        clearArr[v-1] += 1
        
    for i in range(N):
        player = sum(clearArr[i:])
        if player == 0: answer.append([i+1, 0])
        else: answer.append([i+1, clearArr[i] / player])

    return [i for i,v in sorted(answer, key=lambda x: (-x[1], x[0]))]