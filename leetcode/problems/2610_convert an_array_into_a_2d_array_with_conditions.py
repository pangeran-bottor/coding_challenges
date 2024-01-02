from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = {num: 0 for num in nums}
        ans = []

        for num in nums:
            if counts[num] >= len(ans):
                ans.append([])

            counts[num] += 1
            ans[counts[num] - 1].append(num)

        return ans
