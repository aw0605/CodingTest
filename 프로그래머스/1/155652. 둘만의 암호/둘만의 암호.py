def solution(s, skip, index):
    answer = ""
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for v in skip:
        atoz.remove(v)

    for w in s:
        answer += atoz[(atoz.index(w)+index)%len(atoz)]

    return answer