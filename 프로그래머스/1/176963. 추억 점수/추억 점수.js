function solution(name, yearning, photo) {
    let dict = {}
    for (let i = 0; i < name.length; i++){
        dict[name[i]] = yearning[i]
    }
    return photo.map(v => v.reduce((a,c) => dict[c]? a+dict[c] : a,0));
}