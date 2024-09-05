def get_nearlist(m, n, x1, y1, x2, y2):
    symmetry_points = []
    min_distance = m**2 + n**2

    if x1 != x2 or y1 < y2: symmetry_points.append((x1, -y1))
    if x1 != x2 or y1 > y2: symmetry_points.append((x1, n + n - y1))
    if y1 != y2 or x1 < x2: symmetry_points.append((-x1, y1))
    if y1 != y2 or x1 > x2: symmetry_points.append((m + m - x1, y1))
    
    for x, y in symmetry_points:
        min_distance = min(min_distance, (x - x2)**2 + (y - y2)**2)

    return min_distance

def solution(m, n, start_x, start_y, balls):
    return [get_nearlist(m, n, start_x, start_y, x, y) for x, y in balls]
