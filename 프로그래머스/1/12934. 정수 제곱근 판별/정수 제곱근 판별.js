function solution(n) {
    const x = n ** (0.5);
    return x % 1 === 0? (x+1)**2 : -1;
}