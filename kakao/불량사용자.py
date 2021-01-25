import re
import copy

# 최단거리 문제는 보통 BFS가 유리하다.
# 단 path를 다 기억해야하는 경우에는 DFS 방식을 사용하는 것이 좋다
# https://devuna.tistory.com/32 '적합'

def solution(user_id, banned_id):
    answer = [[] for i in range(len(banned_id))]

    # 각 banned_id와 매칭되는 id들을 저장
    for idx, ban_id in enumerate(banned_id):
        pattern = ban_id.replace('*', '.')
        for user in user_id:
            matched = re.match(pattern, user)
            if matched and len(matched.group()) == len(user):
                answer[idx].append(user)

    # 제재 아이디 목록 후보군 저장할 리스트
    global candidates
    candidates = []

    # dfs 탐색
    counter = dfs(answer)

    return counter

def dfs(answer, level = 0, stack = []):
    counter = 0

    # break point
    if level >= len(answer):
        set_stack = set(stack)          # set => 중복제거를 위해서 set([a, b]) == set([b, a])
        if set_stack not in candidates: # 이미 만들어놓은 제재 아이디 목록이 아니라면 카운트
            candidates.append(set_stack)
            return 1
        else: return 0

    # 현재 level
    for user_id in answer[level]:
        # 만약에 현재 탐색하는 user_id가 이미 현재 만들고 있는 아이디 목록에 있으면 의미 없기 때문에 넘어간다.
        if user_id in stack: continue
        stack.append(user_id)
        # 한 레벨 더 내려가서 다음 id 선택
        counter += dfs(answer, level + 1, copy.deepcopy(stack))
        # backtracking
        stack.pop()
    return counter

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
