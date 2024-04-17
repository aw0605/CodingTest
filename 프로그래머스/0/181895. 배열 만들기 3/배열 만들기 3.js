function solution(arr, [[a1,b1],[a2,b2]]) {
    let arr1 = arr.slice(a1,b1+1);
    let arr2 = arr.slice(a2,b2+1); 
    return arr1.concat(arr2)
}