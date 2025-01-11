import sys
input = sys.stdin.readline

n = int(input())
for i in range(1,n+1):
    s = input().strip()
    ans = ""
    for v in s:
        val = ord(v) + 1
        if val > 90: val = 65
        ans += chr(val)
    print(f"String #{i}")
    print(ans)
    print()