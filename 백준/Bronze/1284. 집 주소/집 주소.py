import sys
input = sys.stdin.readline

while True:
    num = input().strip()
    if num == "0": break
    ans = 2 + (len(num) - 1)
    for n in num:
        if n == "0": ans += 4
        elif n == "1": ans += 2
        else: ans += 3
    print(ans)