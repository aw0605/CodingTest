function solution(id_list, report, k) {
    let dec_dict = {}
    let dec_count = {}
    for (let id of id_list) {
        dec_dict[id] = [];
        dec_count[id] = 0;
    }
    
    for (let user of report){
        let [uId, dcId] = user.split(" ");
        dec_dict[dcId].push(uId);
    }
    
    id_list.forEach((v) => {
        dec_dict[v] = [...new Set([...dec_dict[v]])];
        if(dec_dict[v].length >= k){
            dec_dict[v].forEach(i => dec_count[i]++);
        }
    });

    return Object.values(dec_count);
}