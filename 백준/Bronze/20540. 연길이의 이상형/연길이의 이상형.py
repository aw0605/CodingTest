dic = {
    "E": "I", "N": "S", "F": "T", "J": "P",
    "I": "E", "S": "N", "T": "F", "P": "J",
}

mbti = input()
ans = ""
for v in mbti:
    ans += dic[v]
    
print(ans)