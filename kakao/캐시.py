import heapq
def solution(cacheSize, cities):
    answer = 0
    caches = []

    for priority, city in enumerate(cities):
        if cache_check(priority, city, caches):
            answer += 1
            heapq.heapify(caches)
            print(1)
        else:
            answer += 5
            heapq.heappush(caches, (priority, city))
            print(5)

        while len(caches) > cacheSize:
            heapq.heappop(caches)
        print(caches)

    print(answer)
    return answer

def cache_check(target_priority, target_city, caches):
    for idx, cache in enumerate(caches):
        priority, city = cache
        # print(type(city))
        # print(type(target_city))
        print(str(city).lower())
        if str(city).lower() == str(target_city).lower():
            caches[idx] = (target_priority, target_city)
            return True

    return False

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))