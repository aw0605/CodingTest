def solution(s):
    if len(s) == 1: return 1
    min_len = 1000
    
    for i in range(1, len(s) // 2 + 1):
        str1 = ''
        str2 = ''
        ans = ''
        count = 1
        for j in range(0, len(s), i):
            if j == 0: str1 = s[j:j + i]
            else:
                str2 = s[j:j + i]
                if str1 == str2:
                    count += 1
                    if j + i == len(s): ans += f'{count}{str1}'
                else:
                    if count > 1: ans += f'{count}{str1}'
                    else: ans += str1
                    count = 1
                    if len(str1) > len(str2): ans += str2
                    str1 = str2
                    if j + i == len(s): ans += str2
        min_len = min(len(ans), min_len)
    
    return min_len
