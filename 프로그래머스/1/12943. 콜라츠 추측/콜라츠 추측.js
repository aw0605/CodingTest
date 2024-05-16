function solution(num) {
    let i = 0;
    if (num === 1) return 0
    while (num !== 1 && i < 500){
        if (num % 2){
            num = num * 3 + 1
        } else {
            num /= 2
        }
        i++
    }
    return i === 500? -1 : i;
}