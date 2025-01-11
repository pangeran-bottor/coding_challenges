from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _backtrack(ans, visited, curr):
            if len(curr) == len(nums):
                ans.append(curr)
                return
            for idx in range(len(nums)):
                if idx in visited:
                    continue
                visited.add(idx)
                _backtrack(ans, visited, curr + [nums[idx]])
                visited.remove(idx)

        visited = set()
        ans = []
        _backtrack(ans, visited, [])
        return ans
