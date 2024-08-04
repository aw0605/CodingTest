function solution(number, k) {
    let answer = [];

    for (let n of number) {
        while (k > 0 && answer.length && answer[answer.length - 1] < n) {
            answer.pop();
            k--;
        }
        answer.push(n);
    }

    return answer.slice(0, answer.length - k).join('');
}
