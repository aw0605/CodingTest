def solution(s):
    words = s.lower().split(" ")
    answer = [word[0].upper()+word[1:] if word else "" for word in words]
    return " ".join(answer)