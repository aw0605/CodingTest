
function gcd(w, h) {
    if (h == 0) return w
    else return gcd(h, w % h)
}

function solution(w, h) {
    const gcdN = gcd(w, h);
    
    return w * h - (w + h - gcdN);
}