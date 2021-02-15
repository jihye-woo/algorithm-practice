def solution(money):

    if len(money) == 3:
        return max(money[0], money[1], money[2])

    # 첫 번째 집을 방문하는 경우
    include_first = [money[0]]
    include_first.append(max(money[0], money[1]))

    for i in range(2, len(money) - 1):
        include_first.append(max(include_first[i - 2] + money[i], include_first[i - 1]))

    # 첫 번째 집을 방문하지 않는 경우
    exclude_first = [0, money[1]]

    for i in range(2, len(money)):
        exclude_first.append(max(exclude_first[i - 2] + money[i], exclude_first[i - 1]))

    return max(include_first[-1], exclude_first[-1])
