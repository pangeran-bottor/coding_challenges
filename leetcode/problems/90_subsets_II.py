from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def generate(idx, cur):
            if tuple(cur) not in seen:
                ans.append(list(cur))
                seen.add(tuple(cur))

            for i in range(idx, n):
                cur.append(nums[i])
                generate(i + 1, cur)
                cur.pop()

        nums.sort()
        seen = set()
        n = len(nums)
        ans = []
        generate(0, [])
        return ans
