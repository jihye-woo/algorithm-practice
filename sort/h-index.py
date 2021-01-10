def solution(citations):
    citations.sort()
    length = len(citations)
    for idx in range(length):
        num_of_citation = citations[idx]
        num_of_paper = length - idx
        if num_of_citation >= num_of_paper:
            return num_of_paper

    return 0