import sys
input = sys.stdin.readline

m,d,y,t = input().strip().split()
d,y = int(d[:-1]), int(y)
hour, minute = map(int, t.strip().split(":"))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthsDay =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if y%400 == 0 or (y%4 == 0 and y%100 != 0): monthsDay[1] += 1

i = 0
totalD = 0
while months[i] != m:
    totalD += monthsDay[i]
    i += 1
    
totalD += d-1

totalMin = totalD*24*60 + hour*60 + minute
yearMin = sum(monthsDay) * 24 * 60

print(totalMin / yearMin * 100)