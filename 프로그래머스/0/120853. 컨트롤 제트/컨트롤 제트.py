def solution(s):
    nArr = []
    for v in (s.split(" ")):
        if v == "Z": nArr.pop()
        else: nArr.append(v)
    return sum(int(v) for v in nArr)