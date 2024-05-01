function solution(num_list) {
    let odd = 0;
    let even = 0;
    num_list.map(v => v % 2? odd++ : even++)
    return [even, odd];
}