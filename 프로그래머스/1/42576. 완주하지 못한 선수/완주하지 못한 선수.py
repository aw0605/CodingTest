def solution(participant, completion):
    dict = {}
    
    for a in participant:
        dict[a] = dict.get(a, 0) + 1

    for b in completion:
        dict[b] -= 1
        if dict[b] == 0: del dict[b]

    return list(dict.keys())[0]
