# my result summary: https://app.codility.com/demo/results/trainingMAUDXQ-5ET/

def solution(A):
    # write your code in Python 3.6
    def get_leader(A):
        num_counts = {}
        for num in A:
            if num not in num_counts:
                num_counts[num] = 0
            num_counts[num] += 1

        N = len(A)
        for num, count in num_counts.items():
            if count > N//2:
                return num, count
        return None, None

    leader, total_count = get_leader(A)
    if leader is None and total_count is None:
        return 0

    pre = []
    count = 0
    for idx, num in enumerate(A):
        if num == leader:
            count += 1
        pre.append(count)

    ans = 0
    N = len(pre)
    for idx, leader_count in enumerate(pre):
        len_left = idx+1
        len_right = N-len_left

        if (leader_count > len_left//2) and \
           ((total_count-leader_count) > len_right//2):
            ans += 1
    return ans
