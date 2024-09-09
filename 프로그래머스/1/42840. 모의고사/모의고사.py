def solution(answers):
    answer = []
    scores = [0,0,0]
    patterns = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    
    for i, a in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if a == pattern[i % len(pattern)]: scores[j] += 1
            
    for i, v in enumerate(scores):
        if v == max(scores): answer.append(i+1)
    
    return answer