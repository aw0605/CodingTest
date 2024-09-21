def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        sales = amount[i] * 100
        cur = seller[i]
        while sales > 0 and cur != "-":
            total[cur] += sales - (sales//10)
            cur = parent[cur]
            sales //= 10
            
    return [total[name] for name in enroll]