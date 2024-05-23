function solution(nums) {
    return Math.min(Math.trunc(nums.length/2), [...new Set(nums)].length);
}