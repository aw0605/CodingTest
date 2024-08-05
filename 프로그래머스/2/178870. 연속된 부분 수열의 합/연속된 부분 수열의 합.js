function solution(sequence, k) {
    let answer = [0, sequence.length];
    let s = 0;
    let sum = 0;
    
    if (sequence.indexOf(k) != -1) return [sequence.indexOf(k), sequence.indexOf(k)]
    
    for (let i = 0; i < sequence.length; i++) {
        sum += sequence[i];

        while (sum >= k) {
            if (sum === k) {
                if (i - s < answer[1] - answer[0]) {
                    answer = [s, i];
                }
            }
            sum -= sequence[s];
            s++;
        }
    }
    
    return answer;
}