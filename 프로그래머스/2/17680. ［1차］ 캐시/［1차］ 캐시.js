function solution(cacheSize, cities) {
    let cache = []
    let time = 0;
    
    cities.forEach(v => {
        const city = v.toLowerCase();
        if (cacheSize) {
            if (!cache.includes(city)){
                if (cache.length == cacheSize) cache.shift()
                cache.push(city)
                time += 5
            } else {
                cache.splice(cache.indexOf(city),1)
                cache.push(city)
                time++
            }
        } else time += 5
    })
    
    return time;
}