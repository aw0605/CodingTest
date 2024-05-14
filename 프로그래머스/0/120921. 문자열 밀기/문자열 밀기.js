function solution(A, B) {
    let aArr = [...A];
    if (A === B) return 0;
    for (let i = 1; i < aArr.length; i++){
            aArr.unshift(aArr.pop());
            if (aArr.join("") === B) return i
    }
    return -1;
}