def solution(myString):
    return ''.join([v if v > "l" else "l" for v in myString])