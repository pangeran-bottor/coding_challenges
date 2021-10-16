# my result summary: https://app.codility.com/demo/results/training6JSNVF-GKG/

def solution(A):
    # write your code in Python 3.6
    ans = 0
    east_count = 0
    for car in A:
        if car == 0:
            east_count += 1
        else:
            if ans + east_count > 10**9:
                return -1
            ans += east_count
    return ans
