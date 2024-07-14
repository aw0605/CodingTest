function solution(land) {
    for (let i = 1; i < land.length; i++) {
        for (let j = 0; j < land[0].length; j++) {
            let sliceArr = land[i-1].slice(0,j).concat(land[i-1].slice(j+1));
            land[i][j] += Math.max(...sliceArr);
        }
    }
    return Math.max(...land[land.length - 1]);
}