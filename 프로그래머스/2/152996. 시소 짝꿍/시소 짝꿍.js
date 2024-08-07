function solution(weights) {
    let answer = 0;
    const dict = {};
    
    for (let w of weights) dict[w] = (dict[w] || 0) + 1;

    for (let w in dict) {
        answer += dict[w] * (dict[w] - 1) / 2;
        answer += dict[w] * (dict[w * 4 / 3] || 0); 
        answer += dict[w] * (dict[w * 4 / 2] || 0);
        answer += dict[w] * (dict[w * 3 / 2] || 0);
    }
    
    return answer;
}
