function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

function solution(numbers) {
    const answer = new Set();
    let nums = numbers.split('');

    const getPermutation = (arr, fix) => {
        for (let i = 0; i < arr.length; i++) {
            const copy = [...arr];
            const newN = +(fix + arr[i]);
            copy.splice(i, 1);
            if (!answer.has(newN) && isPrime(newN)) answer.add(newN);
            getPermutation(copy, fix + arr[i]);
        }
    };

    getPermutation(nums, '');
    return answer.size;
}
