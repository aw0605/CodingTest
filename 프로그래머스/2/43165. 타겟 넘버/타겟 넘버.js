function solution(numbers, target) {
    let answer = 0;
    const len = numbers.length;
    
    function dfs(i, total) {
        if (i == len) {
            if (total == target) answer++
        } else {
            dfs(i+1, total+numbers[i])
            dfs(i+1, total-numbers[i]) 
        }
    }
    
    dfs(0,0)
    return answer;
}