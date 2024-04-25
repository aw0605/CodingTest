function solution(arr1, arr2) {
    const len1 = arr1.length;
    const len2 = arr2.length;
    if (len1 === len2){
        let sum1 = arr1.reduce((a,c) => a + c, 0);
        let sum2 = arr2.reduce((a,c) => a + c, 0);
        return sum1 === sum2? 0 : (Math.max(sum1, sum2) === sum1? 1 : -1)
    }
    return Math.max(len1, len2) === len1? 1 : -1
}