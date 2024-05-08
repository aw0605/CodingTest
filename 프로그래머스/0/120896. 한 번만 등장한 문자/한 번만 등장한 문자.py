def solution(s):
    answer = []
    for v in s:
        if s.index(v) == s.rindex(v): answer.append(v)
    return ''.join(sorted(answer))