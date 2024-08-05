def solution(sequence, k):
    answer = None
    start, end = 0, 0
    arr = [sequence[0]]
    for i in range(1, len(sequence)):
        num = sequence[i] + arr[-1]
        arr.append(num)

    while start <= end and end < len(sequence):
        s = arr[start]
        e = arr[end]
        val = e - s + sequence[start]

        if val == k:
            if answer is None: answer = [start, end]
            else:
                if (answer[1] - answer[0]) > (end - start): answer = [start, end]

        if val > k: start += 1
        else: end += 1

    return answer