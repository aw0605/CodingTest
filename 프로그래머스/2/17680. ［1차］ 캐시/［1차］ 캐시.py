def solution(cacheSize, cities):
    cache = []
    time = 0
    
    for city in cities:
        city = city.lower()
        if cacheSize:
            # cache miss: 오래된 값 제거 후, 새로운 값 cache에 저장
            if not city in cache:
                if len(cache) == cacheSize: cache.pop(0)
                cache.append(city)
                time += 5
            # cache hit: cache에서 기존 값 제거 후, 맨 뒤에 다시 저장
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        else: time += 5
        
    return time