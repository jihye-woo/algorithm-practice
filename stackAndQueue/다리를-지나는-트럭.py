from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weights_sum = 0
    bridge_weights = deque([])
    truck_weights = deque(truck_weights)
    overlapped = 0

    while truck_weights:
        # 1. make a sub-sequence
        if bridge_weights_sum + truck_weights[0] <= weight:
            target = truck_weights.popleft()
            bridge_weights.append(target)
            bridge_weights_sum += target
        # 2. count sub-sequence period and pop sub-sequence for the next element
        else:
            print(bridge_weights)
            print('answer ', answer)
            # 2-1. count sub-sequence period
            # 2-1-1. consider overlapping period
            if len(bridge_weights) > 1:
                answer += bridge_length + len(bridge_weights) - 1

            # 2-1-2. length of the sub-sequnce is 1,
            #        do not need to consider overlapping
            else: answer += bridge_length

            # 2-2. pop sub-sequence for the next element
            num_of_poping = 0
            while bridge_weights:
                bridge_weights_sum -= bridge_weights.popleft()
                num_of_poping += 1
                if bridge_weights_sum + truck_weights[0] <= weight: break
            overlapped = 0 if len(bridge_weights) == 0 else num_of_poping
            answer -= overlapped

            # 2-1. count sub-sequence period
            # 2-1-1. consider overlapping period
    if len(bridge_weights) > 1:
        answer += bridge_length + len(bridge_weights) - 1
        # 2-1-1. length of the sub-sequnce is 1,
        #        do not need to consider overlapping
    elif len(bridge_weights) == 1: answer += bridge_length

    return answer + 1
