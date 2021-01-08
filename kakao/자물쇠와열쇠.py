def solution(key, lock):
    # Brute Force Searching
    answer = True
    zero_count = count_zero_in_lock(lock)

    if zero_count == 0: return True

    for i in range(4):
        if brute_force(lock, key, zero_count): return True
        key = rotate(key)
    return False

def brute_force(lock, key, zero_count):
    N, M = len(lock), len(key)
    start = -M + 1
    end = N
    # key의 (0,0) 지점은 -M + 1 부터 N 까지 탐색한다
    for x in range(start, end):
        for y in range(start, end):
            if check(x, y, key, lock, zero_count): return True
    return False

def check(start_x, start_y, key, lock, zero_count):
    N, M = len(lock), len(key)

    # key_x, key_y : key의 절대적 인덱스
    # x + start_x, y + start_y : lock을 기준으로 했을 때 key의 상대적 인덱스
    # => 현재 키의 모든 격자를 돌면서 자물쇠와 맞물리는 곳 탐색
    for key_x in range(M):
        for key_y in range(M):
            # 인덱스 x와 y가 모두 자물쇠와 맞물린다면
            lock_x = key_x + start_x
            lock_y = key_y + start_y
            if (0 <= lock_x < N) and (0 <= lock_y < N):
                # 채워넣기 실패한 경우 바로 fasle
                if key[key_y][key_x] + lock[lock_y][lock_x] != 1:
                    return False
                # 채워넣을 경우 lock의 zero 갯수 감소
                elif key[key_y][key_x] == 1:
                    zero_count -= 1

    # 만약 lock의 모든 홈이 채워졌다면 True
    return (zero_count == 0)

def rotate(key):
    return list(zip(*key[::-1]))

def count_zero_in_lock(lock):
    return sum([row.count(0) for row in lock])