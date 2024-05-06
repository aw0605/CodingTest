def solution(order):
    clap = ["3","6","9"]
    answer = 0
    for v in str(order):
        if v in clap: answer += 1
    return answer