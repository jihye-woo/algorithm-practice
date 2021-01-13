def solution(brown, yellow):
    answer = [0, 0]
    N_multi_M = yellow
    N_plus_M = (brown // 2) - 2

    for N in range(1, N_plus_M):
        M = N_plus_M - N
        if (N * M == N_multi_M): return [ M + 2, N + 2 ]

    return answer
