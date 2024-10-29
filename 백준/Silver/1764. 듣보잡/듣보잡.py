import sys
input = sys.stdin.readline

n,m = map(int, input().split())
no_listen = set([input().strip() for _ in range(n)])
no_seen = set([input().strip() for _ in range(m)])
    
ans = sorted(no_listen & no_seen)

print(len(ans))
print("\n".join(ans))


    
