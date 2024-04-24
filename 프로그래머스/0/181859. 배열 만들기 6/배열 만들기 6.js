function solution(arr) {
    let stk = [];
    for (let i = 0; i < arr.length; i++){
        if (stk[stk.length - 1] !== arr[i]){
            stk.push(arr[i]);
        } else if (stk[stk.length - 1] === arr[i]){
            stk.pop();
        }
    }
    return stk.length? stk : [-1];
}