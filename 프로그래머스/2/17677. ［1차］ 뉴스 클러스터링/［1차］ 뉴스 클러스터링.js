function solution (str1, str2) {

    function slice_str(s) {
        const arr = [];
        for (let i = 0; i < s.length - 1; i++) {
            const str = s.slice(i, i+2);
            if (str.match(/[A-Za-z]{2}/)) arr.push(str.toLowerCase());
        }
        return arr;
    }

    const arr1 = slice_str(str1);
    const arr2 = slice_str(str2);
    
    const set = new Set([...arr1, ...arr2]);
    
    let union = 0;
    let intersection = 0;

    for (let v of set){
        const c1 = arr1.filter(x => x === v).length;
        const c2 = arr2.filter(x => x === v).length;
        union += Math.max(c1, c2);
        intersection += Math.min(c1, c2);
    }
    
    return union === 0 ? 65536 : Math.floor(intersection / union * 65536);
}