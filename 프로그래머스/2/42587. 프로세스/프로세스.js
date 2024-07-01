function solution(priorities, location) {
    let total = priorities.length;
    let answer = 0;
    let cur = 0;
    
    while (true) {
        if (Math.max(...priorities) === priorities[cur % total]){
            priorities[cur % total] = 0;
            answer++;
            if ((cur % total) === location) break;
        }
        cur++;
    }
    
    return answer;
}