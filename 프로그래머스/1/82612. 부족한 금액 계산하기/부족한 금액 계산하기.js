function solution(price, money, count) {
    let total = new Array(count).fill(0).reduce((a,_,i) => a + (price * (i+1)), 0)

    return money - total > 0? 0 : total - money;
}