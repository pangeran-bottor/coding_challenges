# my result summary: https://app.codility.com/demo/results/trainingE2BDBK-E72/

def solution(S, P, Q):
    # write your code in Python 3.6
    def add_arr(arr1, arr2):
        return [a1+a2 for a1, a2 in zip(arr1, arr2)]

    def sub_arr(arr1, arr2):
        return [a1-a2 for a1, a2 in zip(arr1, arr2)]

    dna_idx = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }
    pre = [[0, 0, 0, 0, 0]]
    for dna in S:
        new_elem = [0] * 5
        new_elem[dna_idx[dna]] += 1
        pre.append(add_arr(pre[-1], new_elem))

    ans = []
    for p, q in zip(P, Q):
        diff_arr = sub_arr(pre[q+1], pre[p])
        for dna in "ACGT":
            idx = dna_idx[dna]
            if diff_arr[idx] > 0:
                ans.append(idx)
                break

    return ans
