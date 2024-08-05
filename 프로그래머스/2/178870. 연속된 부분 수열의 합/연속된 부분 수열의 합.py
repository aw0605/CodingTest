def solution(sequence, k):
    dic = {i:v for i,v in enumerate(sequence)}
    answer = []
    start, sum = 0,0

    for i,v in enumerate(sequence):
        end = i
        sum += v
        while sum > k :
            sum -= dic[start]
            start += 1
        if sum == k: answer.append([start,end])

    answer.sort(key = lambda x: (x[1]-x[0],x[0]))
    return answer[0]