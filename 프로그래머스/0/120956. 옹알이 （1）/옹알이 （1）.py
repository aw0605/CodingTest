import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    possible = 0
    for w in babbling:
        if regex.match(w):
            possible += 1
    return possible