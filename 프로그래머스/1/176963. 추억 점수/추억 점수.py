def solution(name, yearning, photo):
    return [sum(yearning[name.index(x)] for x in v if x in name) for v in photo]