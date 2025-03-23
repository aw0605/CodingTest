from datetime import datetime
import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
i,j,k = map(int, input().split())
res = (datetime(i,j,k) - datetime(a,b,c)).days

if res >= 365243: print("gg")
else: print(f"D-{res}")