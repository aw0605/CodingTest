def solution(cards1, cards2, goal):
    for v in goal:
        if v in cards1:
            if v == cards1[0]: cards1.pop(0)
            else: return "No"
        elif v in cards2:
            if v == cards2[0]: cards2.pop(0)
            else: return "No"
    return "Yes"