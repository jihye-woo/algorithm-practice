from collections import defaultdict
def solution(clothes):
    answer = 1
    # set : to avoid the same clothingㅎ
    spy_closet = defaultdict(set)

    for clothing in clothes:
        name, category = clothing
        spy_closet[category].add(name)

    for category, set_of_clothing in spy_closet.items():
        answer = answer * (len(set_of_clothing) + 1)

    # except possibility for (0, 0, 0, 0)
    return answer - 1