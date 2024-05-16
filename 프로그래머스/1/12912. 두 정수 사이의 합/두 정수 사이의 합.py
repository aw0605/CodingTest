def solution(a, b):
    s = min(a, b)
    e = max(a, b)
    return sum(v for v in range(s,e+1))