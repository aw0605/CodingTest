def solution(cards):
    answer = []
    
    for i in range(len(cards)):
        group = 0
        while cards[i]:
            ni = cards[i] - 1
            cards[i], i = 0, ni
            group += 1
        answer.append(group)
        
    answer.sort()
    return answer[-1] * answer[-2]