def solution(order):        
    return sum(5000 if "latte" in v else 4500 for v in order)