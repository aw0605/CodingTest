def solution(num, total):
    middle = ((total // num) + 1) if total % num else (total // num)
    return [i + middle - num//2 for i,_ in enumerate([0] * num)]