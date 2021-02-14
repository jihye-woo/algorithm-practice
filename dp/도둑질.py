
def solution(money):
    memo = money.copy()
    memo[0] = max(dp(1, memo), dp(2, memo) + memo[0])

    return memo[0]

def dp(n, memo):
    if n >= len(memo):
        return 0

    return max(dp(n + 1, memo), dp(n + 2, memo) + memo[n])


