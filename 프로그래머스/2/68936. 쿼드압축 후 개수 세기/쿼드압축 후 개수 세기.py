def solution(arr):
    answer = [0, 0]

    def check(x, y, size):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        divideLen = size // 2
                        check(x, y, divideLen)
                        check(x + divideLen, y, divideLen)
                        check(x, y + divideLen, divideLen)
                        check(x + divideLen, y + divideLen, divideLen)
                        return
            answer[first] += 1

    check(0, 0, len(arr))

    return answer
