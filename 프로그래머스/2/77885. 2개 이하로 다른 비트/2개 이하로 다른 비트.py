def f(number):
    bin_num = bin(number)[2:]

    if '0' not in bin_num:
        return int('10' + bin_num[1:], 2)

    bin_num = list(bin_num)
    for i in range(len(bin_num)):
        if bin_num[-i-1] == '0':
            bin_num[-i-1] = '1'
            break

    if i > 0:
        bin_num[-i] = '0'

    return int(''.join(bin_num), 2)


def solution(numbers):
    answer = [f(number) for number in numbers]
    return answer