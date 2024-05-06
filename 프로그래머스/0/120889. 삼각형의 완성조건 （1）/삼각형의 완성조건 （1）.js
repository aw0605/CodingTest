function solution(sides) {
    const maxSide = Math.max(...sides)
    return sides.reduce((a,c) => a + c, 0) - maxSide > maxSide? 1 : 2;
}