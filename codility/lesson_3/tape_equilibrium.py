# my result summary: https://app.codility.com/demo/results/trainingJ49YCZ-DJK/

def solution(A):
    # write your code in Python 3.6
    ans = float("inf")
    N = len(A)
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, N):
        cur_diff = abs(A[i-1] - (A[N-1]-A[i-1]))
        ans = min(ans, cur_diff)
    return ans
