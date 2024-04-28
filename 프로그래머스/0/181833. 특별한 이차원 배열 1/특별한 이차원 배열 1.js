function solution(n) {
    let newArr = Array(n).fill(Array(n).fill(0));
    return newArr.map((v1,i) => {
        return v1.map((v2,j) => j == i? 1 : 0)
    })
}