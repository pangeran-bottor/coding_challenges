# my result summary: https://app.codility.com/demo/results/training7J6X7J-3KS/

def solution(X, Y, D):
    # write your code in Python 3.6
    return ((Y-X) // D) + (1 if (Y-X) % D != 0 else 0)
