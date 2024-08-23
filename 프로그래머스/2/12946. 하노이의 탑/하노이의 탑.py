def solution(n):
    answer = []
    
    def hanoiTop(n, s, e, by):
        if n == 1:
            answer.append([s,e])
            return
        
        hanoiTop(n-1, s, by, e);
        answer.append([s, e]);
        hanoiTop(n-1, by, e, s);
        
    hanoiTop(n, 1, 3, 2)
    
    return answer