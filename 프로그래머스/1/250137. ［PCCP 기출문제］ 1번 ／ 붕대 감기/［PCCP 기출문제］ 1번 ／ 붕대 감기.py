def solution(bandage, health, attacks):
    hp = health
    time, recovery, bonus = bandage
    start = 1
    
    for t, attack in attacks:
        # 공격받기 전까지의 hp계산
        hp += ((t - start) // time) * bonus + (t - start) * recovery
        # 공격받은 후로 start 초기화
        start = t + 1
        # 최대 회복량 설정
        if hp >= health: hp = health
        # 체력에서 피해량만큼 감소
        hp -= attack
        if hp <= 0: return -1
    
    return hp