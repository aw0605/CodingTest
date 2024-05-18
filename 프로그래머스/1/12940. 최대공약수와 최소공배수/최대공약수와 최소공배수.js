function solution(n, m) {
    let gcd;
    let lcm;
    // 최대공약수
    for (let i = Math.min(n,m); i >= 1; i--){
        if ((n % i) === 0 && (m % i) === 0){
            gcd = i;
            break;
        }
    }
    // 최소공배수
    lcm = (n * m) / gcd
    
    return [gcd, lcm];
}