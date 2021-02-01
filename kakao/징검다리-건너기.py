import math
def solution(stones, k):
    answer = 0
    _max = max(stones)
    _min = 0

    while _min < _max: # min_k == max_k 일 때 종료
        _mid = math.ceil((_max + _min) / 2)
        if is_possible(stones, k, _mid):
            _min = _mid
        else:
            _max = _mid - 1

    # is_possible에서 카운트 해준 값이 0일 경우이기 때문에
    return _min + 1

def is_possible(stones, k, _mid):
    max_cnt = 0
    local_cnt = 0 # 연속적으로 0 이하가 나오는 구간을 카운트
    for stone in stones:
        if (stone - _mid) > 0:
            if local_cnt > 0:
                max_cnt = max(local_cnt, max_cnt)
                local_cnt = 0
        else:
            local_cnt += 1
            if local_cnt >= k: return False
    return True

print(solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
