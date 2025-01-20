S = input()

ans = ""
for s in S:
    if s.isalpha():
        if s.islower(): ans += chr((ord(s) - 97 + 13) % 26 + 97)
        else: ans += chr((ord(s) - 65 + 13) % 26 + 65)
    else: ans += s

print(ans)