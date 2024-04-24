function solution(arr, flag) {
    let X = [];
    flag.map((v, i) => {
        if (v === true) {
            for (let j = 1; j <= arr[i]*2; j++){
                X.push(arr[i])
            }

        } else {
            for (let k = 1; k <= arr[i]; k++){
                X.pop()
            }
        }
    })
    return X;
}