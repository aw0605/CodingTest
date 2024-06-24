function solution(clothes) {
    let answer = 1;
    
    const clo_Obj = {};
    for (let arr of clothes) {
        clo_Obj[arr[1]] = (clo_Obj[arr[1]] || 0) + 1;
    }

    for (let key in clo_Obj) answer *= (clo_Obj[key] + 1);

    return answer - 1;
}