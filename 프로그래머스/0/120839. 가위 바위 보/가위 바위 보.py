def solution(rsp):
    arr = {
        "2":"0",
        "0":"5",
        "5":"2"
    }
    return ''.join([arr[v] for v in rsp])