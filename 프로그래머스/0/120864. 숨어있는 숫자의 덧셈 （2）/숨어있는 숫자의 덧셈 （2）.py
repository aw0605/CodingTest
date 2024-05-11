def solution(my_string):
    string = ''.join(v if v.isdigit() else " " for v in my_string).split()
    return sum(int(v) for v in string)