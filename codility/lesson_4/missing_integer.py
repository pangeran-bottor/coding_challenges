# my result summary: https://app.codility.com/demo/results/trainingR7M83P-AAJ/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    counters = [0] * (N + 1)
    for num in A:
        if 0 < num <= N:
            counters[num] += 1

    for i in range(1, N+1):
        if counters[i] == 0:
            return i
    return N+1
