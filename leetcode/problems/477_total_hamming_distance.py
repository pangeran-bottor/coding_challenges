from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits = [[0, 0] for _ in range(32)]
        
        for num in nums:
            for bit in bits:
                bit[num % 2] += 1
                
                num = num // 2
        
        return sum(x*y for x, y in bits)
