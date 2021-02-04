from collections import deque

def solution(gems):
    gem_list = dict()
    queue = deque()
    candidates = [[0,0]]

    # gems의 모든 보석을 순회
    for i in range(len(gems)):
        gem = gems[i]

        # 현재 보석은 이미 발견한 보석
        if gem in gem_list:
            # 보석을 큐에 넣어준다.
            queue.append((gem, i))
            # 현재 큐에 있는 보석들의 갯수 업데이트
            gem_list[gem] += 1
            # 큐의 앞에서부터 필요없는 보석들을 pop
            while queue:
                current = queue[0][0]
                # 큐의 맨 앞에있는 보석이 큐에 이미 있다면(앞자리 이외에도) pop
                if gem_list[current] > 1:
                    queue.popleft()
                    # 현재 큐에 있는 보석들의 갯수 업데이트
                    gem_list[current] -= 1
                else: break

            front = queue[0][1]

            if candidates:
                answer = candidates[0]
                # 만약 후보들보다 길이가 짧다면, 다 지우고 새로운 값을 넣어준다.
                if i - front < answer[1] - answer[0]:
                    candidates = [[front, i]]
                # 만약 후보들과 길이가 같다면 새로운 값을 뒤에 추가해서 넣어준다.
                elif i - front == answer[1] - answer[0]:
                    candidates.append([front, i])
            else:
                candidates = [[front, i]]
        else:
            queue.append((gem, i))
            gem_list[gem] = 1
            new_min = queue[0][1]
            candidates.clear()
            candidates.append([new_min, i])

    answer = candidates[0]
    return [answer[0] + 1, answer[1] + 1]

