def solution(lines):
    set1 = set(i for i in range(lines[0][0], lines[0][1]))
    set2 = set(i for i in range(lines[1][0], lines[1][1]))
    set3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((set1 & set2) | (set2 & set3) | (set1 & set3))