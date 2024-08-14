import sys
def solution(N, road, K):
    visited, D, r = [False]*(N+1), [sys.maxsize]*(N+1), [[(None, None)]] + [[] for _ in range(N)]
    
    for e in road:
        r[e[0]].append((e[1],e[2]))
        r[e[1]].append((e[0],e[2]))
    D[1] = 0
    
    for _ in range(1,N+1): 
        min_ = sys.maxsize
        for i in range(1,N+1): 
            if not visited[i] and D[i] < min_:
                min_ = D[i]
                m = i
                
        visited[m] = True
        
        for w, wt in r[m]:
            if D[m] + wt < D[w]: D[w] = D[m] + wt

    return len([d for d in D if d <= K])