function solution(num, k) {
    let kIdx = num.toString().indexOf(k);
    return kIdx === -1? -1 : kIdx + 1;
}