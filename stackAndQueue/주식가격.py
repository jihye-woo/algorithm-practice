def solution(prices):
    length = len(prices)
    answer = [0 for i in range(length)]

    for i in range(length -1):
        target = prices[i]
        for j in range(i + 1, length):
            answer[i]+=1
            if prices[j] - target < 0: break

    return answer