import sys

n = int(sys.stdin.readline())

def get_count(n,y,w,d1,d2):
    count = 0
    if y == n: count += 1
    else:
        for i in range(n):
            if w[i] or d1[i+y] or d2[i-y+n]: continue
            w[i] = d1[i+y] = d2[i-y+n] = True
            count += get_count(n,y+1,w,d1,d2)
            w[i] = d1[i+y] = d2[i-y+n] = False
    return count

ans = get_count(n, 0, [False]*n, [False]*(n*2), [False]*(n*2))
print(ans)