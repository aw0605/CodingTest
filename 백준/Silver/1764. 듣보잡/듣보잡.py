import sys
data = sys.stdin.read().splitlines()

n, m = map(int, data[0].split())
no_listen = set(data[1:n+1])
no_seen = set(data[n+1:n+1+m])

ans = sorted(no_listen & no_seen)

print(len(ans))
print("\n".join(ans))