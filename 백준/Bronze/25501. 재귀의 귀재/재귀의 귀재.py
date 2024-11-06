import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

def recursion(s,l,r,count):
    count += 1
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

for s in arr:
    res, count = isPalindrome(s)
    print(res, count)
    