import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    deployed, front = 1, -1
    work_days = deque([])

    for progress, speed in zip(progresses, speeds):
        work_day = (math.ceil((100 - progress) / speed))
        if front < 0: front = work_day
        elif front < work_day:
            answer.append(deployed)
            front, deployed = work_day, 1
        else: deployed +=1

    answer.append(deployed)

    return answer