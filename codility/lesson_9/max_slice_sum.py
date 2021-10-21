# my result summary: https://app.codility.com/demo/results/trainingRQ4VNV-R6S/

def solution(A):
    # write your code in Python 3.6
    ans = float("-inf")
    running_max = 0
    for num in A:
        running_max = max(num, running_max + num)
        ans = max(ans, running_max)
    return ans
