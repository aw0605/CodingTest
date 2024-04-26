def solution(rank, attendance):
    a,b,c = sorted([(v, i) for i, v in enumerate(rank) if attendance[i]])[:3]
    return 10000 * a[1] + 100 * b[1] + c[1]