def solution(arr, query):
    for i,v in enumerate(query):
        if i % 2 == 0: 
            del arr[v+1:]
        else: del arr[0:v]
    return arr