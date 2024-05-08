def solution(s):
    return "".join(sorted([ v for v in s if s.count(v) == 1]))