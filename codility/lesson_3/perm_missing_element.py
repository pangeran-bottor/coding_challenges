# my result summary: https://app.codility.com/demo/results/trainingTEXE6E-RWY/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    sum_a = sum(A)
    return (N+2)*(N+1)//2 - sum_a
