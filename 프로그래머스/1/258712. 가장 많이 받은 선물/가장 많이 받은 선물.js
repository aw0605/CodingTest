function solution(friends, gifts) {
    let max = 0;
    // 선물 준 사람을 key, 받은 사람 배열을 value로 하는 객체
    let gt_dict = new Map();
    // 각 사람 별 선물 지수 객체
    let n_dict = new Map();

    friends.forEach(v => {
        gt_dict.set(v, []);
        n_dict.set(v, 0);
    })

    gifts.forEach(gift => {
        let [give, take] = gift.split(" ")
        // 선물 받은 사람들 value로 배열에 넣기
        gt_dict.get(give).push(take);
        // 선물 준 사람들은 +1
        n_dict.set(give, n_dict.get(give)+1);
        // 선물 받은 사람들은 -1
        n_dict.set(take, n_dict.get(take)-1);
    })
    
    for(let i = 0; i < friends.length; i++){
        let count = 0;
        for(let j = 0; j < friends.length; j++){
            // i가 j에게 준 갯수
            let give = gt_dict.get(friends[i]).filter((v) => v == friends[j]).length;
            // i가 j에게 받은 갯수
            let take = gt_dict.get(friends[j]).filter((v) => v == friends[i]).length;
            // 준 것 > 받은 것이면 i의 count++
            if(give > take) count++;
            // 주고 받은 수가 같지만 i의 선물 지수가 더 크면 count++
            else if(give == take){
                if(n_dict.get(friends[i]) > n_dict.get(friends[j])) count++;
            }
        }
        // 가장 많이 받은 선물 수 업데이트
        if(count > max) max = count;
    }

    return max;
}