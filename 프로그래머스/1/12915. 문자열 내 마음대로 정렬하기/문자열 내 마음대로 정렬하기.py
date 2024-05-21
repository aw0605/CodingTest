def solution(strings, n):
    return sorted(strings, key = lambda v: v[n]+v)