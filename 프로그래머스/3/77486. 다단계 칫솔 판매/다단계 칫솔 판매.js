function solution(enroll, referral, seller, amount) {
    let answer = [];
    let map = new Map();

    for (let i = 0; i < enroll.length; i++){
        map.set(enroll[i], {parents : referral[i], sales: 0 });
    }

    for (let i = 0; i < seller.length; i++){
        let num = amount[i] * 100;
        let sell = seller[i];

        while (true){
            let data = map.get(sell);
            let share = parseInt(num / 10);

            map.set(sell, {parents : data.parents, sales : data.sales + num-share}); 

            if (data.parents === '-') break;
            if (share === 0) break;
            sell = data.parents;
            num = share;
        }
    }

    for (let [_, v] of map) answer.push(v.sales);

    return answer;
}
