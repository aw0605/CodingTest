from itertools import product

def solution(users, emoticons):
    sale_percent = [10, 20, 30, 40]
    emo_len = len(emoticons)
    result = [0, 0]
    cases = list(product(sale_percent, repeat=emo_len))

    for cur_case in cases:
        emoticon_plus = 0
        sum_price = 0

        for buy_percent, buy_plus in users:
            price = 0
            et_plus_flag = False
            
            for et, discount in zip(emoticons, cur_case):
                if discount >= buy_percent: price += et * (100 - discount) / 100 
                if price >= buy_plus:
                    et_plus_flag = True
                    break
            
            if et_plus_flag: emoticon_plus += 1
            else: sum_price += price

        if emoticon_plus > result[0]:
            result[0] = emoticon_plus
            result[1] = sum_price
        elif emoticon_plus == result[0] and sum_price > result[1]:
            result[1] = sum_price
    
    return result
