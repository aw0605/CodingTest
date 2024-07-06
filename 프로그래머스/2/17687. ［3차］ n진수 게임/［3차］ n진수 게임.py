DIGITS = list('0123456789ABCDEF')

def n2base(n, base):
    digits = []
    
    if n == 0: return DIGITS[0]
    while n > 0:
        digits.append(DIGITS[n % base])
        n //= base

    return ''.join(digits[::-1])


def solution(n, t, m, p):
    digits = []
    turn = 0
    
    while len(digits) < t * m:
        digits += list(n2base(turn, n))
        turn += 1
        
    return ''.join(digits[p-1::m][:t])