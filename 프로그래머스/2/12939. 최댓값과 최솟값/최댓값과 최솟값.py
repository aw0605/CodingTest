def solution(s):
    intArr = [int(n) for n in s.split(" ")]
    return f'{min(intArr)} {max(intArr)}'