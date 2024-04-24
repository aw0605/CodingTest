import re

def solution(myStr):
    result = [v for v in re.split("[a-c]", myStr) if v]
    if len(result) == 0: return ["EMPTY"]
    else: return result