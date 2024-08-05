function solution(sequence, k) {
    let answer = null;
    let sum = sequence[0];
    let s = 0, e = 0;

    while (s < sequence.length && e < sequence.length) {
        if (sum === k) {
            if (answer == null || e - s < answer[1] - answer[0]) {
                answer = [s, e];
            }
        }
        if (sum < k || s == e) sum += sequence[++e];
        else sum -= sequence[s++];
    }

    return answer;
}