def solution(s):
    enNum = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i,v in enumerate(enNum):
        if v in s: s = s.replace(v,str(i))
    return int(s)