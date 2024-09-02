function solution(info, query) {
    let answer = [];

    function combi(arr, selectNum) {
        const result=[];
        if (selectNum === 1) return arr.map((v)=>[v]);
        else {
            arr.forEach((v, i)=>{
                const fixed = v;
                const restArr = arr.slice(i+1);
                const combiArr = combi(restArr, selectNum-1);
                const mergeArr = combiArr.map((v)=>[fixed, ...v]);
                result.push(...mergeArr);
            });
            return result;
        }
    };

    function bsGo(arr, tgt) {
        let left = 0, right = arr.length;
        
        while (left < right){
            const mid = parseInt((left+right)/2);
            if (arr[mid] < tgt) left = mid+1;
            else right = mid;
        }
        return left;
    }

    const info_score = new Map();
    info_score.set("", []);

    info.forEach(v => {
        val = v.split(" ");
        const score = val[val.length-1];
        val.pop();
        info_score.get("").push(+score);

        for (let i = 1; i <= 4; i++) {
            const comb = combi("0123".split(""), i);
            comb.forEach((i)=>{
                const key = i.map((v) => val[+v]).join("");
                if (info_score.has(key)) info_score.get(key).push(+score);
                else info_score.set(key, [+score]);
            });
        }
    });
    
    for (const [key, v] of info_score) v.sort((a, b) => a - b)

    query.forEach((v)=>{
        v = v.replace(/\sand\s|\-/gi, "").split(" ");
        const key = v[0];
        const score =+ v[1];
        if (info_score.has(key)) {
            const scores = info_score.get(key);
            const index = bsGo(scores, score);
            answer.push(scores.length-index);
        } else answer.push(0);
    });

    return answer;
}