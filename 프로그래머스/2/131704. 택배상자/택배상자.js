function solution(order) {
    let answer = 0;
    let n = 1;
    const stack = [];
    
    while (true) {
        if (order.length === answer) break;
        if (order[answer] === n) {
            answer++;
            n++;
        } else if (stack[stack.length - 1] === order[answer]){
            stack.pop();
            answer++;
        } else if (stack[stack.length - 1] !== order[answer]) {
            if (order[answer] < stack[stack.length - 1]) break;
            stack.push(n);
            n++;
        }
    }

    return answer;
}