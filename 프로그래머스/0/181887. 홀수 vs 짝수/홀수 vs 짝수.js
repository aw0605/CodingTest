function solution(num_list) {
    let odd = 0;
    let even = 0;
    for (let i = 1; i < num_list.length+1; i++){
        if (i % 2 !== 0){
            odd += num_list[i-1]
        } else {
            even += num_list[i-1]
        }
    } 
    return odd >= even? odd : even;
}