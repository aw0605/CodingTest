import sys
input = sys.stdin.readline

arr = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]

p = int(input())
for _ in range(p):
    t = input()
    ans = [0] * 8
    for i in range(len(t)-2):
        seq = t[i:i+3]
        if seq in arr: ans[arr.index(seq)] += 1
    print(*ans)