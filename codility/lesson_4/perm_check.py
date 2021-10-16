# my result summary: https://app.codility.com/demo/results/trainingZAVWRX-292/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    cur_set = set()
    for num in A:
        if num > N:
            return 0
        if num in cur_set:
            return 0
        cur_set.add(num)
    return 1
