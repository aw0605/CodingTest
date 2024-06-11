function solution(bandage, health, attacks) {
    const [time, recovery, bonus] = bandage;
    let start = 1;
    let hp = health;
    
    for (let [t, attack] of attacks){
        hp += (Math.trunc((t - start)/time) * bonus) + ((t - start) * recovery);
        start = t + 1
        if (hp >= health) hp = health;
        hp -= attack;
        if (hp <= 0) return -1
    }
    
    return hp;
}

