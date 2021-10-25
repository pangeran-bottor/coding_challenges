# my result summary: https://app.codility.com/demo/results/trainingNK6MU8-5QN/

def solution(A):
    # write your code in Python 3.6
    def generate_fibs(N):
        fibs = [1, 2]
        while fibs[-1] + fibs[-2] <= N:
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

    if len(A) == 0:
        return 1

    A.append(1)
    N = len(A)
    dp = [-1] * N
    fibs = generate_fibs(N)
    for fib in fibs:
        if A[fib-1] == 1:
            dp[fib-1] = 1

    for idx in range(N):
        if A[idx] == 0 or dp[idx] > 0:
            continue

        min_idx = -1
        min_val = 100000
        for fib in fibs:
            prev_idx = idx - fib
            if prev_idx < 0:
                break
            if 0 < dp[prev_idx] < min_val:
                min_val = dp[prev_idx]
                min_idx = prev_idx
        if min_idx != -1:
            dp[idx] = min_val + 1
    return dp[-1]
