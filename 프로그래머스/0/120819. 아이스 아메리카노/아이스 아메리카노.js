function solution(money) {
    let americano = Math.floor(money / 5500);
    let change = money % 5500
    return [americano, change]
}