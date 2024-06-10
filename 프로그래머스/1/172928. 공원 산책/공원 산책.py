def find_start(park):
    for y, x in enumerate(park):
        if "S" in x: return [y, x.index("S")]
    return [-1, -1]

def move_location(start, direction, distance, park):
    initial_y, initial_x = start
    y, x = start

    for i in range(distance):
        y += direction[0]
        x += direction[1]
        if 0 <= y < len(park) and 0 <= x < len(park[0]) and park[y][x] != "X":
            continue
        else: return [initial_y, initial_x]
    
    return [y, x]

def solution(park, routes):
    start = find_start(park)
    directions = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}

    for route in routes:
        direction = directions[route[0]]
        distance = int(route[2])

        start = move_location(start, direction, distance, park)

    return start
