function solution(arr, idx) {
    let result = []
    for (let i = idx; i <= arr.length; i++){
        if (arr[i] == 1) result.push(i) 
    }
    return result.length == 0? -1 : result[0] 
}