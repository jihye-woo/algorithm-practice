def solution(array, commands):
    answer = []

    for i, j, k in commands:
        target_array = []
        for idx in range(i - 1, j):
            target_array.append(array[idx])
        target_array.sort()
        kth_num = target_array[k - 1]
        answer.append(kth_num)

    return answer