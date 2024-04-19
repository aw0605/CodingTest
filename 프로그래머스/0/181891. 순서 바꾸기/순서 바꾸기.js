function solution(num_list, n) {
    let front_list = num_list.slice(0,n)
    let back_list = num_list.slice(n)
    return back_list.concat(front_list);
}