def solution(num):
    i = 0
    while (num != 1 and i < 500):
        num = num * 3 + 1 if num % 2 else num / 2
        i += 1
    return i if num == 1 else -1