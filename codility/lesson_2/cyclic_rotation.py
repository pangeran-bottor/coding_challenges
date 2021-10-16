# my result summary: https://app.codility.com/demo/results/trainingV5Q7QQ-GMM/

def solution(A, K):
    # write your code in Python 3.6
    N = len(A)
    result = [0] * N
    for idx, num in enumerate(A):
        new_idx = (idx + K) % N
        result[new_idx] = num
    return result
