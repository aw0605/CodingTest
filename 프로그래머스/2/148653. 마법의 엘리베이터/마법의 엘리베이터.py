def solution(storey):
    answer = 0
    x = list(map(int, str(storey)[::-1]))

    for i in range(len(x)):
        if x[i] < 5: answer += x[i]
        elif x[i] == 5:
            answer += 5
            if i+1 < len(x) and x[i+1] >= 5: x[i+1] += 1 
        else: 
            answer += 10 - x[i]
            if i+1 < len(x): x[i+1] += 1
            else: answer += 1

    return answer