from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def _digit_sum(num):
            sum_ = 0
            while num:
                sum_ += num % 10
                num = num // 10
            return sum_

        ans = -1
        sum_map = {}
        for num in nums:
            digit_sum = _digit_sum(num)
            if digit_sum not in sum_map:
                sum_map[digit_sum] = num
                continue

            ans = max(ans, num + sum_map[digit_sum])
            sum_map[digit_sum] = max(num, sum_map[digit_sum])

        return ans
