import collections

def solution(participant, completion):
    total = collections.Counter()
    total.update(participant)
    total.update(completion)

    for key, val in total.items():
        if val % 2 != 0:
            return key

    return ''
