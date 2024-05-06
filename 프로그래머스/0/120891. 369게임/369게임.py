def solution(order):
    return sum([str(order).count(v) for v in "369"])