def solution(citations):
    answer = 0

    # front, last = 0, max(citations)
    front, last = 0, 10000

    while front < last:
        mid = front + last // 2
        mid_result = sum([1 for c in citations if c >= mid])
        if mid < mid_result:
            front = mid + 1
        else:
            last = mid - 1

    return front + 1

print(solution(	[3, 0, 6, 1, 5]))