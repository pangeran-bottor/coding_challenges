# my result summary: https://app.codility.com/demo/results/training32PRWP-RBZ/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N < 3:
        return 0

    A.sort()
    for i in range(N-2):
        p = A[i]
        q = A[i+1]
        r = A[i+2]

        if (p + q > r and p + r > q and q + r > p):
            return 1
    return 0
