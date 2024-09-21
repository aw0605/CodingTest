function solution(enroll, referral, seller, amount) {
    const parent = {};
    const total = {};

    for (let i = 0; i < enroll.length; i++) {
        parent[enroll[i]] = referral[i];
        total[enroll[i]] = 0;
    }

    for (let i = 0; i < seller.length; i++) {
        let sales = amount[i] * 100;
        let cur = seller[i];

        while (sales > 0 && cur !== "-") {
            total[cur] += sales - Math.floor(sales / 10);
            cur = parent[cur];
            sales = Math.floor(sales / 10);
        }
    }

    return enroll.map(name => total[name]);
}
