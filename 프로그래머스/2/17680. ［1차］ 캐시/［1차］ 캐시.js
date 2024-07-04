function solution(cacheSize, cities) {
    const MISS = 5, HIT = 1;

    if (!cacheSize) return MISS * cities.length;

    let time = 0,
        cache = [];

    cities.forEach(city => {
        city = city.toLowerCase();

        let idx = cache.indexOf(city);

        if (idx !== -1) {
            cache.splice(idx, 1);
            time += HIT;
        } else {
            if (cache.length === cacheSize) cache.shift();
            time += MISS;
        }
        cache.push(city);
    });

    return time;
}