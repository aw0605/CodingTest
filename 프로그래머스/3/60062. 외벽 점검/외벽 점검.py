from itertools import permutations

def solution(n, weak, dist):
    m = len(weak)
    answer = len(dist)+1
    weak = weak + [num+n for num in weak]
    
    for friends in permutations(dist):
        for i in range(m):
            new_weak = weak[i:i+m]
            now = new_weak[0]
            cnt = 0
            for f in friends:
                cnt += 1
                if cnt >= answer: break
                now = now + f
                if now >= new_weak[-1]:
                    answer = cnt
                    break
                else:
                    for w in new_weak:
                        if w > now:
                            now = w
                            break

    return -1 if answer > len(dist) else answer