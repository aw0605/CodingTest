from fractions import gcd

def solution(n, m):
    g = gcd(n,m)
    l = (n*m)//g
    return [g,l]