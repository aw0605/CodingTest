def solution(sides):
    maxSide = max(sides)
    sides.remove(maxSide)
    if sum(sides) > maxSide: return 1
    else: return 2