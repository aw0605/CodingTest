function solution(id_list, report, k) {
    let reports = [...new Set(report)].map(a=>{return a.split(' ')});
    let dec_counts = new Map();
    let mail_counts = new Map();
    
    for (const report of reports){
        dec_counts.set(report[1],dec_counts.get(report[1])+1||1)
    }
    
    for(const report of reports){
        if(dec_counts.get(report[1])>=k){
            mail_counts.set(report[0],mail_counts.get(report[0])+1||1)
        }
    }
    
    return id_list.map(v => mail_counts.get(v)||0);
}