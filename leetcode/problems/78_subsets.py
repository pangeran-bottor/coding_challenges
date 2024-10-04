from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _backtrack(idx: int, curr: list):
            ans.append(list(curr))

            for i in range(idx, n):
                curr.append(nums[i])
                _backtrack(i + 1, curr)
                curr.pop()

        n = len(nums)
        ans: List[List[int]] = []
        _backtrack(0, [])

        return ans
