import re

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if re.match('[a-zA-Z]{2}', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if re.match('[a-zA-Z]{2}', str2[i:i+2])]

    intersection = set(str1) & set(str2)
    union = set(str1) | set(str2)

    if len(union) == 0: return 65536

    intersection = sum(min(str1.count(v), str2.count(v)) for v in intersection)
    union = sum(max(str1.count(v), str2.count(v)) for v in union)

    return int((intersection/union) * 65536)