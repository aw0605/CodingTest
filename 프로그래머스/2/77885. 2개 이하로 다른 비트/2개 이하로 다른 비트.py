def solution(numbers):
    answer = []
    for number in numbers:
        if number & 1:
            target = number
            idx = 0
            while number > 0:
                if number % 2 == 0: break
                number //= 2
                idx += 1
            answer.append(target + 2 ** (idx) - 2 ** (idx-1))
        else: answer.append(number+1)

    return answer