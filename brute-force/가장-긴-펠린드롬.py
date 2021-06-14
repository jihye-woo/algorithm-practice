def solution(s):
    answer = 0 if len(s) == 0 else 1

    for start in range(0, len(s) - 1):
        for end in range(len(s) - 1, start, -1):
            if end - start + 1 < answer: break
            if s[start] == s[end] and is_palindrome(start, end, s):
                answer = max(end - start + 1, answer)

    return answer

def is_palindrome(start, end, s):
    while start < end:
        if s[start] != s[end]: return False
        start += 1
        end -= 1
    return True

print(solution(	"abcdcba"))


