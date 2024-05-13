def solution(before, after):
    return 1 if ''.join(sorted(v for v in before)) == ''.join(sorted(v for v in after)) else 0