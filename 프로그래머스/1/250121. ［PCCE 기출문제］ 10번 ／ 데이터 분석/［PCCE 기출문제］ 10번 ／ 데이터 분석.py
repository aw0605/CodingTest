def solution(data, ext, val_ext, sort_by):
    answer = []
    division = ["code", "date", "maximum", "remain"]
    for v in data:
        if v[division.index(ext)] < val_ext: answer.append(v)

    answer.sort(key=lambda x: x[division.index(sort_by)])
    return answer