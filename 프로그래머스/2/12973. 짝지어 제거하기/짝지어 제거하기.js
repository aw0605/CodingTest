function solution(s){
    let stack = [];

    for (let v of s){
        if(stack[stack.length-1] === v) stack.pop()
        else stack.push(v)
    }

    return stack.length === 0 ? 1 : 0;
}