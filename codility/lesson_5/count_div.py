# my result summary: https://app.codility.com/demo/results/trainingD5DYRP-9YA/

def solution(A, B, K):
    # write your code in Python 3.6
    all_div = B // K
    partial_div = (A-1) // K
    return all_div - partial_div
