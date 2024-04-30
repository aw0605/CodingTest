function solution(n) {
    let i = 1;
    while ((n*i) % 6){i++}
    return (n*i) / 6;
}