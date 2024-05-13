def solution(id_pw, db):
    for v in db:
        if id_pw[0] == v[0]:
            if id_pw[1] == v[1]:
                return "login"
            else: return "wrong pw"
    return "fail"