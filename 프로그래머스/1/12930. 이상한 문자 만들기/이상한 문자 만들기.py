def solution(s):
    return ' '.join(''.join([x.lower() if i % 2 else x.upper() for i, x in enumerate(v)]) for v in s.split(" "))