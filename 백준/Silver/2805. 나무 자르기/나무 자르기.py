import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
s, e = 0, max(trees)

def get_total(h):
    return sum(tree - h if tree > h else 0 for tree in trees)

while s <= e:
    mid = (s + e) // 2
    if get_total(mid) >= m: s = mid + 1
    else: e = mid - 1

print(e)
