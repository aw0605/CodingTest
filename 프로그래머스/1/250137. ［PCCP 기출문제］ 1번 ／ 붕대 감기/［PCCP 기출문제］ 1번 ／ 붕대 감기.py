def solution(bandage, health, attacks):
    time, recovery, bonus = bandage
    max_health = health
    cur_health = health
    series = 0
    
    attack_dict = {t: attack for t, attack in attacks}
    
    for i in range(1, attacks[-1][0] + 1):
        if i in attack_dict:
            cur_health -= attack_dict[i]
            series = 0
            if cur_health <= 0: return -1
        else:
            cur_health += recovery
            series += 1
            if series == time:
                cur_health += bonus
                series = 0
            if cur_health > max_health: cur_health = max_health
    
    return cur_health
