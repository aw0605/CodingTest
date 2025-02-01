import sys

input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

arr = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]

cnt = 0
ans = ""
for i in range(0, len(s), 6):
    S = s[i:i+6]
    cnt += 1
    if S in arr: ans += chr(arr.index(S) + 65)
    else:
        closest_char = None
        for j in range(8):
            diff = sum(1 for k in range(6) if S[k] != arr[j][k])
            if diff <= 1:
                closest_char = chr(j + 65)
                break
        if closest_char: ans += closest_char
        else:
            print(cnt)
            exit()

print(ans)