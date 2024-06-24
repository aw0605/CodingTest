function solution(clothes) {
    return Object.values(clothes.reduce((obj, v)=> {
        obj[v[1]] = obj[v[1]] ? obj[v[1]] + 1 : 1;
        return obj;
    } , {})).reduce((a,c)=> a * (c+1), 1) - 1;    
}