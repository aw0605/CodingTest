function solution(k, score) {
    let result = []
    let answer = [];
    for (let v of score){
        result.push(v);
        result.sort((a,b) => b-a);
        if (result.length > k) result.pop();
        answer.push(Math.min(...result));
    }
    return answer;
}