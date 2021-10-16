# my result summary: https://app.codility.com/demo/results/training3GY6SA-Y2Q/

def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * (N+1)
    cur_max = 0
    moving_max = 0
    for num in A:
        if num == N+1:
            cur_max = moving_max
        else:
            counters[num] = max(counters[num], cur_max) + 1
            moving_max = max(moving_max, counters[num])

    for i in range(1, N+1):
        cur_val = counters[i]
        if cur_val < cur_max:
            counters[i] = cur_max
    return counters[1:]
