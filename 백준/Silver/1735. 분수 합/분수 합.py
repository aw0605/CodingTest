import math
import sys
data = sys.stdin.read().splitlines()

a,b = map(int, data[0].split())
c,d = map(int, data[1].split())

y = math.lcm(b,d)
a *= y//b
c *= y//d
x = a + c

gcdN = math.gcd(x,y)

print(x//gcdN, y//gcdN)

