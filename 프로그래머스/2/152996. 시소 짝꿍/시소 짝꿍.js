function solution(weights) {
    let answer = 0;
    const dict = new Map();
    for (const weight of weights) dict.set(weight, (dict.get(weight) || 0) + 1);

    for (const [weight, count] of dict.entries()) {
        answer += (count * (count - 1)) / 2;
        answer += count * (dict.get(weight * 4 / 3) || 0);
        answer += count * (dict.get(weight * 4 / 2) || 0);
        answer += count * (dict.get(weight * 3 / 2) || 0);
    }

    return answer;
}
