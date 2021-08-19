from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_1, max_2 = 0, 0
        min_1, min_2 = float("inf"), float("inf")

        for num in nums:
            if num >= max_1 and num >= max_2:
                max_2 = max_1
                max_1 = num
            elif max_1 >= num and num >= max_2:
                max_2 = num

            if num <= min_1 and num <= min_2:
                min_2 = min_1
                min_1 = num
            elif min_1 <= num and num <= min_2:
                min_2 = num

        ans = max_1*max_2 - min_1*min_2
        return ans
