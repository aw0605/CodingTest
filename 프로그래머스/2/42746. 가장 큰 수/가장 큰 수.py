import functools

def compare(a,b):
    c1 = a+b
    c2 = b+a
    return (int(c1) > int(c2)) - (int(c1) < int(c2))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(compare),reverse=True)
    return str(int(''.join(n)))