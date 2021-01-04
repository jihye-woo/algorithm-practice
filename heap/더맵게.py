import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    lowest = heapq.heappop(scoville)
    while scoville:
        if lowest >= K: break
        second_lowest = heapq.heappop(scoville)
        new_scoville = lowest + (second_lowest * 2)
        answer += 1
        lowest = heapq.heappushpop(scoville, new_scoville)

    return answer if lowest >= K else -1