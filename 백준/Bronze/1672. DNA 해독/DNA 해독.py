import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())

dic = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", 
       "GA" : "C", "GG" : "G", "GC" : "T", "GT" : "A", 
       "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
       "TA" : "G", "TG" : "A", "TC" : "G","TT" : "T"}

while len(s) > 1:
    sub = s.pop() + s.pop()
    s.append(dic[sub[::-1]])
            
print(s[0])