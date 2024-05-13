function solution(score) {
    let averageArr = score.map(v => (v[0] + v[1]) / 2);
    let sortArr = [...averageArr].sort((a,b) => b - a);
    return averageArr.map(v => sortArr.indexOf(v) + 1);
}