from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for v in permutations(range(len(dungeons))):
        hp = k
        L = 0
        for i in v:
            x, y = dungeons[i]
            if hp >= x:
                hp -= y
                L += 1
        answer = max(answer, L)


    return answer