import sys
data = sys.stdin.read().splitlines()

a,b = map(int, data[0].split())
aArr = set(map(int, data[1].split()))
bArr = set(map(int, data[2].split()))

ans = aArr^bArr

print(len(ans))