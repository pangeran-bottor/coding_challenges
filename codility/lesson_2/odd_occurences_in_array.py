# my result summary: https://app.codility.com/demo/results/trainingH4RUWV-WZA/

def solution(A):
    # write your code in Python 3.6
    cur = 0
    for num in A:
        cur ^= num
    return cur
