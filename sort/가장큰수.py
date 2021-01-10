from functools import cmp_to_key
def solution(numbers):
    answer = ''
    numbers = [str(num) for num in numbers]
    numbers.sort(key = cmp_to_key(compare))

    for num in numbers:
        answer += num

    return str(int(answer))

def compare(item1, item2):
    new_str1 = item1 + item2
    new_str2 = item2 + item1
    if new_str1 > new_str2:
        return -1
    elif new_str1 < new_str2:
        return 1
    else: return 0