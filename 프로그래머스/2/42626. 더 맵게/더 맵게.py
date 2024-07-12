from collections import deque

def solution(scoville, K):
    answer = 0 
    mix = deque()
    scoville.sort()
    sco = deque(v for v in scoville)
    
    while (sco and sco[0] < K) or (mix and mix[0] < K):
        if len(sco) + len(mix) <= 1: return -1
        
        food = [0] * 2
        for i in range(2):
            if sco and mix:
                if sco[0] < mix[0]: food[i] = sco.popleft()
                else: food[i] = mix.popleft()
            elif sco: food[i] = sco.popleft()
            else: food[i] = mix.popleft()
            
        mix.append(food[0]+food[1]*2)
        answer += 1
        
    return answer