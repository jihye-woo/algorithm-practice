def solution(name):
    ascii_val_A, ascii_val_Z = 65, 90
    up_and_down, left_and_right = 0, len(name) - 1

    for c in name:
        num_of_up = ord(c) - ascii_val_A
        up_and_down += ascii_val_Z - ord(c) + 1 if num_of_up > 13 else num_of_up

    right_most_A = count_continuousA(reversed(name))
    left_most_A = count_continuousA(name[1:])

    left = up_and_down + left_and_right - right_most_A
    right = up_and_down + left_and_right - left_most_A

    return min(left, right)

def count_continuousA(name, counter = 0):
    for c in name:
        if c != 'A': break
        counter += 1
    return counter

print(solution(	"BBBAAAAB"))