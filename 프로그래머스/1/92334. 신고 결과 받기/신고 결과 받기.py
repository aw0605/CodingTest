def solution(id_list, report, k):
    mail_counts = [0] * len(id_list)
    dec_counts = {id:0 for id in id_list}
    
    for r in set(report): dec_counts[r.split(" ")[1]] += 1

    for r in set(report):
        reporter, reported = r.split(" ")
        if dec_counts[reported] >= k:
            mail_counts[id_list.index(reporter)] += 1
            
    return mail_counts