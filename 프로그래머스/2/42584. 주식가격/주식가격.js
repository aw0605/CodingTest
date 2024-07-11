function solution(prices) {
    let answer = new Array(prices.length).fill(0);
    let stack = []
    
    for (let i = 0; i < prices.length; i++){
        while (stack.length && stack[stack.length-1][1] > prices[i]){
            let [past, _] = stack.pop();
            answer[past] = i - past;
        }
        stack.push([i,prices[i]])
    }
    
    for (let [i, _] of stack) answer[i] = prices.length - 1 - i
    
    return answer;
}