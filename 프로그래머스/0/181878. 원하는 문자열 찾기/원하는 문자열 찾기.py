def solution(myString, pat):
    if (myString.upper()).find(pat.upper()) != -1:
        return 1
    return 0