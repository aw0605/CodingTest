function solution(num) {
    let i = 0;
    while (num !== 1 && i < 500){
        num % 2? num = num * 3 + 1 : num /= 2
        i++
    }
    return num === 1? i : -1;
}