function solution(my_string) {
    const numArr = my_string.match(/[0-9]+/g)
    return numArr? numArr.reduce((a,c) => a + +c,0) : 0
}