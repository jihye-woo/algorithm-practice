from collections import deque
def solution(numbers):
    answer = ''
    numbers = [str(num) for num in numbers]
    numbers = reversed_sort(numbers)

    for num in numbers:
        answer += num
    return answer

def reversed_sort(numbers):
    sorted_list = deque([])
    for num in numbers:
        if not sorted_list: sorted_list.append(num)
        else: insert_num(num, sorted_list)
    return sorted_list

def insert_num(num, sorted_list):
    insert_here = False
    for idx in range(len(sorted_list)):
        target = sorted_list[idx]
        if need_to_check(target, num):
            insert_here = is_larger(target, num)
        else: insert_here = target < num

        if insert_here:
            sorted_list.insert(idx, num)
            return

    sorted_list.append(num)
    return


def need_to_check(target, num):
    return target[0] == num[0] and len(target) != len(num)

def is_larger(target, num):
    len_diff = len(target) - len(num)
    if len_diff < 0:
        return target + (target[0] * -len_diff) < num
    else: return target < num + (num[0] * len_diff)


print(solution(	[3, 30, 34, 5, 9]))