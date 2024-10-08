from functools import reduce

def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    return reduce(lambda x, y: x ^ y,
                  [sum(map(lambda x: x%(i+1), data[i])) for i in range(row_begin-1, row_end)])