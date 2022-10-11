from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1, nums2):
            merged = []
            l, r = 0, 0
            n1, n2 = len(nums1), len(nums2)
            
            while l < n1 and r < n2:
                if nums1[l] <= nums2[r]:
                    merged.append(nums1[l])
                    l += 1
                else:
                    merged.append(nums2[r])
                    r += 1
                
            if l < n1:
                merged += nums1[l:]
            if r < n2:
                merged += nums2[r:]
            return merged
        
        def merge_sort(nums):
            if len(nums) == 1:
                return nums
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        ans = merge_sort(nums)
        return ans
