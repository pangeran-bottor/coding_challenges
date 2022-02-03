from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        N = len(nums1)
        
        first_half_counts = {}
        for n1 in nums1:
            for n2 in nums2:
                first_half_counts[n1+n2] = first_half_counts.get(n1+n2, 0) + 1
        
        result = 0
        
        for n3 in nums3:
            for n4 in nums4:
                target = -(n3+n4)
                result += first_half_counts.get(target, 0)
                
        return result
