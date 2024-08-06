function solution(storey) {
    if (storey < 10) return Math.min(storey, 11 - storey)
    let left = storey % 10
    return Math.min(left + solution(Math.trunc(storey/10)), 10 - left + solution(Math.trunc(storey/10)+1));
}