# my result summary: https://app.codility.com/demo/results/training2WSD7M-DQ3/

def solution(N):
    # write your code in Python 3.6
    n_binary = "{0:b}".format(N)
    ans = 0
    one_idx = None
    for idx, ch in enumerate(n_binary):
        if ch == "1":
            if one_idx is None:
                one_idx = idx
            else:
                ans = max(ans, idx-one_idx-1)
                one_idx = idx
    return ans
