from collections import defaultdict

def solution(tickets):
    global graph
    global N
    graph = defaultdict(list)
    not_used = defaultdict(int)
    N = len(tickets) + 1

    for ticket in tickets:
        from_where, to_where = ticket
        graph[from_where].append(to_where)
        not_used[(from_where, to_where)] += 1

    answers = dfs('ICN', ['ICN'], not_used)
    answers.sort()
    return answers[0]


def dfs(next, path, not_used):
    answer = []
    if len(path) == N:
        return [path]

    for neighbor in graph[next]:
        ticket = (next, neighbor)
        if ticket in not_used.keys() and not_used[ticket] > 0:
            not_used[ticket] -= 1
            candidate_path_list = dfs(neighbor, path + [neighbor], not_used)
            not_used[ticket] += 1
            answer += candidate_path_list
    return answer

