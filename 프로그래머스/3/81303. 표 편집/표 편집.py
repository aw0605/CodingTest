def solution(n, k, cmd):
    answer = ['O'] * n
    deleted = []
    
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    
    k += 1
    
    for cmdI in cmd:
        if cmdI.startswith("C"):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        elif cmdI.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
            
        else:
            a,num = cmdI.split( )
            if a == "U":
                for _ in range(int(num)): k = up[k]
            else:
                for _ in range(int(num)): k = down[k]
        
    for i in deleted: answer[i-1] = "X"
    
    return "".join(answer)