from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(prev):
            if len(prev) == n:
                ans.append(list(prev))
                return

            for i in range(n):
                if nums[i] in prev:
                    continue
                prev.append(nums[i])
                generate(prev)
                prev.pop()

        n = len(nums)
        ans = []
        generate([])
        return ans
