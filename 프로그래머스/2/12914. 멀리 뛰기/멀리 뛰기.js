function solution(n) {
    if (n === 1) return 1;
    let a = 1, b = 2;
    
    for(let i = 3; i <= n; i++) {
        [a, b] = [b, a];
        b = (a + b) % 1234567;
    }
    
    return b;
}