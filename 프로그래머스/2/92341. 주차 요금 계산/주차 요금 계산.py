from math import ceil

def solution(fees, records):
    answer = []
    parkDict = {}
    dt, df, at, af = fees
    
    for v in records:
        t,n,s = v.split(" ")
        h, m = map(int,t.split(":"))
        t = h * 60 + m
        if n not in parkDict: parkDict[n] = [0, t, s]
        else:
            if s == "IN": parkDict[n][1], parkDict[n][2] = t, s
            else:
                parkDict[n][0] += t - parkDict[n][1]
                parkDict[n][2] = s
    
    for n,v in parkDict.items():
        f = df
        if v[-1] == "IN": 
            v[0] += 1439 - v[1]
            parkDict[n][2] = "OUT"
        if v[0] > dt: f += ceil((v[0]-dt) / at) * af
        answer.append([n,f])
    
    answer.sort(key = lambda x: x[0])
    return [f for n,f in answer]