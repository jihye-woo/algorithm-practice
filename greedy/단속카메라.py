def solution(routes):
    answer = 1
    routes.sort(key=lambda x:x[1])
    last_max_point = routes[0][1]
    for idx in range(1, len(routes)):
        start, end = routes[idx]
        if start > last_max_point:
            last_max_point = end
            answer += 1
    return answer