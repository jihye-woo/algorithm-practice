def solution(name):
    ascii_val_A, ascii_val_Z = 65, 90
    up_and_down, left_and_right = 0, len(name) - 1

    for c in name:
        num_of_up = ord(c) - ascii_val_A
        up_and_down += ascii_val_Z - ord(c) + 1 if num_of_up > 13 else num_of_up

    right_most_A = count_continuousA(reversed(name))
    left_most_A = count_continuousA(name[1:])
    left = left_and_right - right_most_A
    right = left_and_right - left_most_A

    answer = min(left, right)

    max_info = max_continuousA(name)
    idx, max_len = max_info

    if idx > 1: # front 쪽으로 가려고 해도 막혀있뜸
        front = idx - 1
        back = len(name) - (idx + max_len)

        b_f_b = back * 2 + front
        f_b_f = front * 2 + back

        back_track_min = min(b_f_b, f_b_f)
        answer = min(back_track_min, answer)

    return answer + up_and_down
    # left = up_and_down + left_and_right - right_most_A
    # right = up_and_down + left_and_right - left_most_A
    #
    # return min(left, right)

def count_continuousA(name, counter = 0):
    for c in name:
        if c != 'A': break
        counter += 1
    return counter

def max_continuousA(name):
    #(start_idx, max_len)
    max_info = (-1, 0)
    for idx in range(len(name)):
        if name[idx] == 'A':
            length = count_continuousA(name[idx:])
            if max_info[1] < length:
                max_info = (idx, length)
    return max_info
