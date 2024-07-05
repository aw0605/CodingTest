function solution(numbers, target) {
    let answer = 0;

    function dfs(i, total) {
        if (i < numbers.length) {
            dfs(i+1, total + numbers[i]);
            dfs(i+1, total - numbers[i]);
        } else {
            if(total === target) answer++
        }
    }
    
    dfs(0,0);
    return answer;
}