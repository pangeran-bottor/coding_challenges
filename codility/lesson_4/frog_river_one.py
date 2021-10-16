# my result summary: https://app.codility.com/demo/results/trainingF49K2G-968/

def solution(X, A):
    # write your code in Python 3.6
    cur_set = set()
    for idx, num in enumerate(A):
        if num not in cur_set:
            cur_set.add(num)
        if len(cur_set) == X:
            return idx
    return -1
