const check = (n, k, enemy) => {
    enemy.sort((a, b) => b - a)
    const enemySum = enemy.reduce((sum, cur) => sum += cur, 0)
    const kSum = enemy.slice(0, k).reduce((sum, cur) => sum += cur, 0)

    if (enemySum - kSum > n) return false;
    return true;
}

function solution(n, k, enemy) {
    const stack = []
    let start = 0, end = enemy.length, mid;

    while (start < end) {
        mid = Math.floor((start + end) / 2)
        if (check(n, k, enemy.slice(0, mid + 1))) start = mid + 1;
        else end = mid;
    }

    return start;
}
