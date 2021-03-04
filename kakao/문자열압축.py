def solution(s):
    answer = len(s)

    for n in range(1, len(s)):
        local_min = check(n, s)
        answer = min(local_min, answer)

    return answer

# n의 길이단위로 문자열 s를 탐색
# 예를 들어, n = 1 s = aabbaccc
#
# a a b b a c c c, n이 1이므로 길이가 1인 단위로 검사

# a a
# b b
# a c
# c c c

def check(n, s):
    total_len = len(s)
    # 압축 기준이 되는
    idx = 0
    # n = 1d일 때는 idx가
    while idx < len(s) - n + 1:
        idx, count = zip_string(idx, n, s)
        if count > 0:
            total_len -= (count * n)
            total_len += len(str(count + 1)) # 자기자신까지 포함
    return total_len

def zip_string(idx, n, s):
    # 예를 들어, n = 1 s = aabbaccc
    # aababccc
    # a a 검사 매칭 -> count ++
    # a b 검사 매칭 실패 -> return [매칭에 실패한 b의 인덱스, count]

    count = 0
    target = idx + n

    while target < len(s) - n + 1:
        if s[idx:idx + n] != s[target:target + n]:
            break
        count += 1
        target += n
    return target, count

print(solution("aabbaccc"))
