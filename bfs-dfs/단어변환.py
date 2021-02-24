from collections import deque, defaultdict
def solution(begin, target, words):
    global length
    length = len(begin)
    visited = set()

    # 완전 0인 케이스 제외
    if target not in words: return 0

    root_list = find_neighbors(begin, words, 1)
    stack = deque(root_list)
    while stack:
        current, num = stack.pop()
        if current == target:
            return num
        if current not in visited:
            visited.add(current)
            neighbor_list = find_neighbors(current, words, num + 1)
            stack.extend(neighbor_list)
    return 0

def find_neighbors(begin, words, num):
    neighbors = []
    for word in words:
        if edit_number_one(begin, word):
            neighbors.append((word, num))
    return neighbors

def edit_number_one(begin, word):
    n = 0
    for i in range(length):
        if begin[i] != word[i]:
            n += 1
            if n > 1: False
    return (n == 1)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
