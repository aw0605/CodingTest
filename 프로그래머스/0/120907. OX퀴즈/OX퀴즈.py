def solution(quiz):
    answer = []
    for v in quiz:
        cal,value = v.split(" = ")
        X,op,Y = cal.split()
        result =  0
        if op == "+": result = int(X) + int(Y)
        else: result = int(X) - int(Y)
        answer.append("O") if result == int(value) else answer.append("X")
    return answer