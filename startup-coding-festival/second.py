N = int(input())

line = input()
dp = [int(i) for i in line]

for pos in range(2, N):
    dp[pos] *= dp[pos - 1] + dp[pos - 2]

print(dp[N-1])


