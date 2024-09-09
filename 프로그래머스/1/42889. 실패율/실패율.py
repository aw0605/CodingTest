def solution(N, stages):
    players = len(stages)
    fails = {}
    challengers = [0] * (N+2)
    for s in stages: challengers[s] += 1
    
    for i in range(1, N+1):
        if challengers[i] == 0: fails[i] = 0
        else: 
            fails[i] = challengers[i]/players
            players -= challengers[i]
    
    return sorted(fails, key = lambda x: fails[x], reverse = True)