import heapq
from itertools import permutations
def solution(n, weak, dist):
    min_friends = len(dist)

    shifted_lists = []
    for i in range(len(weak)):
        shifted_lists.append(weak)
        largest = weak[0] + n
        weak = weak[1:] + [largest]

    # len(weak)개 부터 1개 까지
    for shifted in shifted_lists:
        for friends in permutations(dist, len(dist)):
            min_friends = min(find_min(shifted, friends), min_friends)
            if min_friends == 1: return min_friends
    return min_friends

def find_min(shifted, friends):
    # a b c d
    start_idx, end_idx = 0, 1
    count_friend = 0

    for friend in friends:
        count_friend += 1

        while shifted[start_idx] - shifted[end_idx] < friend:
            end_idx += 1

        start_idx = end_idx
        end_idx = end_idx + 1
        if end_idx >= len(shifted): # pass case
            return count_friend

    return count_friend