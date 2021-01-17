def solution(n, lost, reserve):
    reserve = set(reserve)
    duplicate = set()
    num_of_lost = len(lost)
    for r in reserve:
        if r in lost:
            duplicate.add(r)
            num_of_lost -= 1

    for l in lost:
        if l in duplicate:
            continue
        elif check_and_remove(l - 1, reserve, duplicate):
            num_of_lost -= 1
        elif check_and_remove(l + 1, reserve, duplicate):
            num_of_lost -= 1

    return n - num_of_lost

def check_and_remove(target, reserve, duplicate):
    if target in reserve and target not in duplicate:  # O(1 + 1)
        reserve.remove(target)
        return True
    return False

