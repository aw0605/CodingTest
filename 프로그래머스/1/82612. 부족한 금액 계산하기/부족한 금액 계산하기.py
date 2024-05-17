def solution(price, money, count):
    total = (price * ((count * (count+1)) // 2)) - money
    return total if total > 0 else 0