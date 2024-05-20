function solution(s){
    return [...s].map((v, i) => {
        const result = s.slice(0, i).lastIndexOf(v);
        return result === -1? -1 : i - result;
    });
}