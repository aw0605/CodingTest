function solution(numbers) {
    let stack = []
    let answer = new Array(numbers.length).fill(-1);
    
    for (let i = 0; i < numbers.length; i++){
        while (stack && numbers[stack[stack.length-1]] < numbers[i]){
            answer[stack.pop()] = numbers[i]
        }
        stack.push(i)
    }
    
    return answer;
}