# my result summary: https://app.codility.com/demo/results/training98GEFH-9P4/

def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A)
    ans = float("-inf")
    ans = max(ans, A[0]*A[1]*A[N-1])
    ans = max(ans, A[N-3]*A[N-2]*A[N-1])
    return ans
