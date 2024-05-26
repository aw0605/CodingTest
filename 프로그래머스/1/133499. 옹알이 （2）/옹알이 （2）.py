def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for v in babbling:
        for w in words:
            if w*2 in v: break;
            v = v.replace(w, " ")
        if v.strip() == "": answer += 1
    return answer