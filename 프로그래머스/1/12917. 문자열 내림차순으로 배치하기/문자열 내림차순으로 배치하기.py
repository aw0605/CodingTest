def solution(s):
    return ''.join([v for v in sorted(s, reverse = True) if not v.isupper()]) + ''.join([v for v in sorted(s, reverse = True) if v.isupper()])