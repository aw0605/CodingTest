import sys
input = sys.stdin.readline

h2, m2, s2 = map(int, input().split(":"))
h1, m1, s1 = map(int, input().split(":"))

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2
t = t1 - t2 if t1 > t2 else t1 - t2 + 86400

h = t//3600
m = t//60 % 60
s = t % 60

print("%02d:%02d:%02d" % (h,m,s))