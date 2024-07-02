from collections import Counter
import re

def solution(str1, str2):
    
    def slice_str(s):
        arr = []
        for i in range(len(s)-1):
            if re.match('[a-zA-Z]{2}', s[i:i+2]): arr.append(s[i:i+2].lower())
        return arr
    
    c1 = Counter(slice_str(str1))
    c2 = Counter(slice_str(str2))
    
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    
    return 65536 if union == 0 else int(intersection / union * 65536)
