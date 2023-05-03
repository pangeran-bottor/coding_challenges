from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_map, nums2_map = {}, {}
        for num in nums1:
            nums1_map[num] = 1
        for num in nums2:
            nums2_map[num] = 1

        ans0, ans1 = [], []
        for num in nums1_map:
            if num not in nums2_map:
                ans0.append(num)
        for num in nums2_map:
            if num not in nums1_map:
                ans1.append(num)
        return [ans0, ans1]
