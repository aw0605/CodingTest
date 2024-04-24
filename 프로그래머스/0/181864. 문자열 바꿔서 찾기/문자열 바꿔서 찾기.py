def solution(myString, pat):
    newString = "".join(["B" if v == "A" else "A" for v in myString])
    if pat in newString: return 1
    else: return 0