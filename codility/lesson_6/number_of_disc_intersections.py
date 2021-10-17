# my result summary: https://app.codility.com/demo/results/trainingUCTDYK-7R5/

from bisect import bisect_right


def solution(A):
    # write your code in Python 3.6
    N = len(A)
    borders = [(idx-r, idx+r) for idx, r in enumerate(A)]
    borders.sort(key=lambda x: (x[0], x[1]))
    lefts = [el[0] for el in borders]
    rights = [el[1] for el in borders]

    ans = 0
    for i in range(N):
        pos = bisect_right(lefts, rights[i])
        ans += (pos - i - 1)

        if ans > 10**7:
            return -1
    return ans


# O(N) solution
# reference:
# https://zhengxucoding.wordpress.com/2015/04/11/codility-numberofdiscintersections/

def solution_linear(A):
    # write your code in Python 3.6
    N = len(A)
    starts = [0] * N
    ends = [0] * N

    for i in range(N):
        start_idx = max(0, i-A[i])
        starts[start_idx] += 1

        end_idx = i + A[i]
        if end_idx < N:
            ends[end_idx] += 1

    ans = 0
    cur_discs = 0
    for i in range(N):
        if starts[i] > 0:
            ans += cur_discs*starts[i]

            ans += (starts[i] * (starts[i] - 1))//2

            if ans > 10**7:
                return -1

            cur_discs += starts[i]
        cur_discs -= ends[i]
    return ans
