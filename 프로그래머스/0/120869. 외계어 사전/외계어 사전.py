def solution(spell, dic):
    for v in dic:
        if not set(spell) - set(v): return 1
    return 2