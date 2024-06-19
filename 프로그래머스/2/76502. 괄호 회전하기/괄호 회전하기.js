function solution(s) {
    if (s.length % 2) return 0;
    
    let stack = [] ;
    let answer = 0; 
    
    for (let i = 0; i < s.length; i++){
        let rotS = s.slice(i) + s.slice(0, i);
        let flag = true
        for (let v of rotS) {
            if (v === "(" || v === "{" || v === "[") stack.push(v)
            else { 
                let acc = stack.pop()
                if(acc === "(" && v === ")") continue;
                if(acc === "{" && v === "}") continue;
                if(acc === "[" && v === "]") continue;
                flag = false;
                break;
            }
        }
        if (flag) answer++;
    }
    
    return answer; 
}