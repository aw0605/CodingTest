s = input().upper()
sDict = {}

for v in s:
    sDict[v] = sDict.get(v, 0) + 1
        
maxVal = [k for k,v in sDict.items() if max(sDict.values()) == v]

print("?" if len(maxVal) > 1 else maxVal[0])