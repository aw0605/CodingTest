def solution(prices):
    answer = []
    tmp = prices[::-1]
    
    while tmp:
        price = tmp.pop()
        sec = 0;
        for i in range(len(tmp)-1, -1, -1):
            sec += 1
            if price > tmp[i]: break
        answer.append(sec)
    
    return answer