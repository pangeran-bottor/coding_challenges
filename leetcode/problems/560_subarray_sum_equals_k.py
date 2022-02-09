from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapper = dict()
        result = 0
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            
            if cur_sum == k:
                result += 1
                
            if cur_sum - k in mapper:
                result += mapper[cur_sum - k]
                
            if cur_sum not in mapper:
                mapper[cur_sum] = 0
            mapper[cur_sum] += 1
        return result
