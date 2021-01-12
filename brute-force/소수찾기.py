from itertools import permutations

def solution(numbers):
    answer = 0
    max_len = len(numbers)
    visited = set()
    numbers = [c for c in numbers]
    for i in range(1, max_len + 1):
        answer += get_num_of_primes(set(permutations(numbers, i)), visited)
    return answer

def get_num_of_primes(num_set, visited):
    answer = 0
    for nums in num_set:
        num = get_num(nums)
        if num in visited: continue
        if is_prime(num): answer += 1
        visited.add(num)
    return answer


def get_num(nums):
    str_num = ''
    for num in nums:
        str_num += num
    return int(str_num)

def is_prime(num):
    if num in [0, 1]: return False
    for i in range(2, num):
        if (num % i == 0): return False
    return True