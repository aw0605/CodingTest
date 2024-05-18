function solution(arr1, arr2) {
    return arr1.map((x, i) => x.map((v, j) => v+arr2[i][j]));
}