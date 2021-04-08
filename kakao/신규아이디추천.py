import re
def solution(new_id):
    answer = ''

    step1 = new_id.lower()

    step2 = re.sub("[^a-z0-9-_.]", '', step1)

    step3 = re.sub('\.{2,}', '.', step2)

    answer = step4 = step3.strip('\.')

    if '' == answer:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('\.')

    while len(answer) < 3:
        answer += answer[-1]

    return answer