# my result summary: https://app.codility.com/demo/results/training3B3R5U-35V/

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    pre = [0]
    for num in A:
        pre.append(pre[-1] + num)

    ans = None
    min_val = float("inf")
    for i in range(2, 4):
        for j in range(i, N+1):
            cur_val = pre[j] - pre[j-i]
            cur_avg = cur_val / i
            if cur_avg < min_val:
                min_val = cur_avg
                ans = j - i
    return ans
