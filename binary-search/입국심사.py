def solution(n, times):
    left = 0
    right = 1_000_000_000_000 * 1_000_000_000 // n + 1
    while left <= right:
        mid = (left + right) // 2
        total = check(mid, times)
        if total >= n:
            right = mid - 1
        else:
            left = mid + 1

    return left

def check(mid, times):
    total = 0
    for time in times:
        total += mid // time
    return total

print(solution(	3, [7, 10]))
