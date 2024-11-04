from collections import Counter
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
counter = Counter([i for _ in range(n) if len(i := input()) > m])

sys.stdout.write(''.join(sorted(counter, key= lambda x: (-counter[x], -len(x), x))))