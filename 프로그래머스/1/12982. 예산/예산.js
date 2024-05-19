function solution(d, budget) {
    return d.sort((a, b) => a - b).reduce((answer, price) => {
        return answer + ((budget -= price) >= 0);
    }, 0);
}