function gcd(n,m){
    while (m) [n, m] = [m, n % m]
    return n
}

function solution(arr) {
    return arr.reduce((a, c) => a * c / gcd(a, c))
}