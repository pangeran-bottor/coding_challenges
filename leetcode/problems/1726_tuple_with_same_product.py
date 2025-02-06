from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        product_map = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product not in product_map:
                    product_map[product] = 0
                product_map[product] += 1

        for product, count in product_map.items():
            ans += count * (count - 1) // 2
        return ans * 8
