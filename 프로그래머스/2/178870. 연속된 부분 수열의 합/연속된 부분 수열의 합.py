def solution(sequence, k):
    answer = []
    s, e = 0, 0
    total = sequence[0]
    min_len = 2147483647
    
    while s <= e < len(sequence):
        if total >= k:
            if total == k and min_len > e - s + 1:
                min_len = e - s + 1
                answer = [s, e]
            total -= sequence[s]
            s += 1
        else:
            e += 1
            if e < len(sequence): total += sequence[e]

    return answer