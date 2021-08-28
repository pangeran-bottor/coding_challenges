from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            if a >= b:
                return gcd(b, a % b)
            else:
                return gcd(b, a)
        min_num, max_num = min(nums), max(nums)
        ans = gcd(max_num, min_num)
        return ans
