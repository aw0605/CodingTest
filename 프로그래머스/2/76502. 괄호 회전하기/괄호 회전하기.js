function solution(s) {
    let answer = 0;
    
    for (let i = 0; i < s.length; i++) {
        const stack = [];
        const rotS = s.slice(i) + s.slice(0, i);
      
        for (let j of rotS) {
            if (stack[stack.length - 1] === "(" && j === ")") stack.pop();
            else if (stack[stack.length - 1] === "[" && j === "]") stack.pop();
            else if (stack[stack.length - 1] === "{" && j === "}") stack.pop();
            else stack.push(j);
        }
        if (!stack.length) answer++;
    }
    
    return answer;
}