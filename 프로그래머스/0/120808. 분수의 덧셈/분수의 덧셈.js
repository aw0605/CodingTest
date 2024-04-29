function solution(numer1, denom1, numer2, denom2) {
    let numer = (numer1 * denom2) + (numer2 * denom1)
    let denom = denom1 * denom2 
    const gcd = (numer, denom) => (numer % denom === 0? denom : gcd(denom, numer % denom));
    return [numer / gcd(numer, denom), denom / gcd(numer, denom)];
}