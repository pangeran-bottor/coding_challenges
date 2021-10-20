# my result summary: https://app.codility.com/demo/results/trainingNPGBQY-QBX/

def solution(A):
    # write your code in Python 3.6
    num_counts = {}
    for idx, num in enumerate(A):
        if num not in num_counts:
            num_counts[num] = []
        num_counts[num].append(idx)

    N = len(A)
    for num, idx_list in num_counts.items():
        if len(idx_list) > N//2:
            return idx_list[0]
    return -1
