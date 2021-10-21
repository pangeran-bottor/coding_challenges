# my result summary: https://app.codility.com/demo/results/trainingXYDEDH-HSZ/

def solution(A):
    # write your code in Python 3.6
    ans = 0
    lowest_price = float("inf")
    for num in A:
        lowest_price = min(lowest_price, num)
        ans = max(ans, num - lowest_price)
    return ans
