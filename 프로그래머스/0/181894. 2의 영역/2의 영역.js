function solution(arr) {
    let slice1 = arr.indexOf(2)
    let slice2 = arr.lastIndexOf(2)

    return slice1 == -1? [-1] : arr.slice(slice1, slice2+1)
}