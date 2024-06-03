def solution(ingredient):
    answer = 0
    burger = []
    
    for v in ingredient:
        burger.append(v)
        if burger[-4:] == [1,2,3,1]:
            answer += 1
            for i in range(4): burger.pop()
    
    return answer