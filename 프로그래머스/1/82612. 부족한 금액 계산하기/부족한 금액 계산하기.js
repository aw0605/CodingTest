function solution(price, money, count) {
    const total = price * (count * (count + 1) / 2) - money;
    return total > 0 ? total : 0;
}