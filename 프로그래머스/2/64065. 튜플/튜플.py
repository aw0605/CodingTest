import re
from collections import Counter

def solution(s):
    s = Counter(re.findall('\d+', s))
    
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))