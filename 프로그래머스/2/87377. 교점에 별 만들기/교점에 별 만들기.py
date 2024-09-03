def solution(line):
    cross = set()
    
    for a in range(len(line)):
        for b in range(len(line)):
            if a == b: continue
            point = getIntCross(line[a], line[b])
            if point: cross.add(point)
    xs, ys = list(map(lambda x: x[0], cross)), list(map(lambda x: x[1], cross))

    startX, startY = min(xs), min(ys)
    height = max(ys) - startY + 1
    width = max(xs) - startX + 1
    cross = list(map(lambda x: (x[0]-startX, x[1]-startY), cross))

    answer = ['.' * width for _ in range(height)]

    for x, y in cross: answer[y] = answer[y][:x]+'*'+answer[y][x+1:]

    return answer[::-1]

def getIntCross(l1, l2):
    a, b, e = l1; c, d, f = l2
    if a*d - b*c == 0: return False
    x = (b*f - e*d) / (a*d - b*c)
    y = (e*c - a*f) / (a*d - b*c)

    return (int(x), int(y)) if x==int(x) and y==int(y) else False