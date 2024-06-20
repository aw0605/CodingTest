function solution(want, number, discount) {
    let answer = 0;
    let item_dict = {};
    for (let i = 0; i < number.length; i++) item_dict[want[i]] = number[i];
    
    for (let i = 0; i <= discount.length-10; i++) {
        let slice = discount.slice(i, i+10);
        let flag = true;
        
        for (let j of want) {
            if (slice.filter((v) => v === j).length !== item_dict[j]) {
                flag = false;
                break;
            }
        }
        if (flag) answer++;
    }
    
  return answer;
}