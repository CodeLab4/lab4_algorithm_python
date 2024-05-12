from collections import deque


def solution(cacheSize, cities):
    answer = 0

    cache_lst = deque()

    for city in cities:
        city = city.lower()

        if city in cache_lst:
            cache_lst.remove(city)
            cache_lst.append(city)
            answer += 1
        else:
            answer += 5
            if len(cache_lst) < cacheSize:
                cache_lst.append(city)
            elif cacheSize > 0:
                cache_lst.popleft()
                cache_lst.append(city)

    return answer