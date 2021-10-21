# my result summary: https://app.codility.com/demo/results/training5X5XDQ-HV5/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    pre = [0] * N
    suf = [0] * N

    for i in range(1, N-1):
        pre[i] = max(pre[i-1] + A[i], 0)
    for i in range(N-2, 0, -1):
        suf[i] = max(suf[i+1] + A[i], 0)

    ans = 0
    for i in range(1, N-1, 1):
        ans = max(ans, pre[i-1] + suf[i+1])
    return ans
