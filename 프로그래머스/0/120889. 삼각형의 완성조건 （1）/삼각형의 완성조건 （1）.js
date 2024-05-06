function solution(sides) {
    const [max, a, b] = sides.sort((a,b) => b-a);
    return max < a + b ? 1 : 2
}