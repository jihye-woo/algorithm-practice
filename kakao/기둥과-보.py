from collections import defaultdict


def solution(n, build_frame):
    answer = []
    built = defaultdict(list)

    for info in build_frame:
        do(info, built)

    for key, values in built.items():
        for value in values:
            answer.append([key[0], key[1], value])
    return sorted(answer) if answer else [[]]


def do(info, built):
    x, y, build_type, is_build = info
    pos = (x, y)

    if is_build:  # 설치
        if build(pos, build_type, built):
            built[pos].append(build_type)

    else:  # is_remove 삭제
        if is_exist(pos, build_type, built):
            remove(pos, build_type, built)


def build(pos, build_type, built):
    x, y = pos
    if build_type == 0:  # 기둥
        if y == 0:
            return True
        elif 0 < y < 1000:  # y가 1000이면 기둥이 1000을 초과해버리므로 y < 1000
            # (x, y)를 기준으로 왼쪽과 오른쪽에 보가 있거나, 아래 기둥이 있다면 True
            return is_exist((x - 1, y), 1, built) or is_exist((x, y), 1, built) or is_exist((x, y - 1), 0, built)

    elif build_type == 1:  # 보
        # 설치하려는 보의
        # 1. 왼쪽이나 오른쪽에 기둥이 있거나
        if bo_has_column(pos, built):
            return True
        # 2. 양 옆에 보가 있거나
        if is_exist((x - 1, y), 1, built) and is_exist((x + 1, y), 1, built):
            return True
    return False


def remove(pos, build_type, built):
    x, y = pos

    built[pos].remove(build_type)

    if build_type == 0:  # 기둥
        candidates = [[(x - 1, y + 1), 1], [(x + 1, y + 1), 1], [(x, y + 1), 0]]
        if not can_removed(candidates, built):
            built[pos].append(build_type)

    else:  # 보
        candidates = [[(x - 1, y), 1], [(x + 1, y), 1], [(x, y), 0], [(x + 1, y), 0]]
        if not can_removed(candidates, built):
            built[pos].append(build_type)

# helper methods

def can_removed(candidates, built):
    for pos, build_type in candidates:
        if not build(pos, build_type, built):
            return False
    return True


def bo_has_column(pos, built):
    x, y = pos
    # 보에게
    # 1. 왼쪽 기둥이 있다.
    if is_exist((x, y - 1), 0, built):
        return True
    # 2. 오른쪽 기둥이 있다.
    if is_exist((x + 1, y - 1), 0, built):
        return True
    # 현재 보 양 옆에는 기둥이 없다.
    return False

def is_exist(pos, build_type, built):
    return pos in built and build_type in built[pos]

