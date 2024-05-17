function solution(s) {
    return s.slice(Math.trunc((s.length-1)/2),Math.trunc(s.length)/2+1);
}