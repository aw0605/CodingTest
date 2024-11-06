import sys

def append_star(n):
    if n == 1: return ['*']

    Stars = append_star(n//3)
    arr = []
    for S in Stars: arr.append(S*3)
    for S in Stars: arr.append(S + ' '*(n//3) + S)
    for S in Stars: arr.append(S*3)
    return arr

n = int(sys.stdin.readline())

print('\n'.join(append_star(n)))
        