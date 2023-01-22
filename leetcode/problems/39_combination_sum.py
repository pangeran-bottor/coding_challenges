from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def backtrack(start_idx, seq):
            if sum(seq) == target:
                ans.append(list(seq))
                return

            if sum(seq) > target:
                return

            for idx in range(start_idx, n):
                seq.append(candidates[idx])
                backtrack(idx, seq)
                seq.pop()

        backtrack(0, [])
        return ans
