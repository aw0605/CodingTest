function solution(order) {
    return [...order.toString()].filter(v => "369".includes(v)).length;
}