from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        dups = set()

        for i, val1 in enumerate(nums):
            if val1 in dups:
                continue
            dups.add(val1)

            seen = set()
            for j, val2 in enumerate(nums[i + 1 :]):
                target = -(val1 + val2)
                if target in seen:
                    ans.add(tuple(sorted((val1, val2, target))))

                seen.add(val2)

        return list(ans)
