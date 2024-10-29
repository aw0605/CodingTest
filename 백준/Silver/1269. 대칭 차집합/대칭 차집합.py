import sys
input = sys.stdin.readline

a,b = map(int, input().split())
aArr = set(map(int, input().split()))
bArr = set(map(int, input().split()))

ans = aArr^bArr

print(len(ans))