def solution(line):
    points = []

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            adbc = a * d - b * c
            
            if adbc != 0:
                x = (b * f - e * d) / adbc
                y = (e * c - a * f) / adbc

                if x.is_integer() and y.is_integer(): points.append((int(x), int(y)))

    if not points: return []

    minX = min(point[0] for point in points)
    maxX = max(point[0] for point in points)
    minY = min(point[1] for point in points)
    maxY = max(point[1] for point in points)

    width = maxX - minX + 1
    height = maxY - minY + 1

    star = [['.'] * width for _ in range(height)]

    for x, y in points: star[maxY - y][x - minX] = '*'

    return [''.join(row) for row in star]
