# my result summary: https://app.codility.com/demo/results/training6929RX-JZ4/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N < 2:
        return N

    A.sort()
    ans = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans += 1
    return ans
