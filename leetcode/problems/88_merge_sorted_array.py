from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n - 1
        l, r = m - 1, n - 1
        while l >= 0 and r >= 0:
            if nums1[l] <= nums2[r]:
                nums1[cur] = nums2[r]
                r -= 1
            else:
                nums1[cur] = nums1[l]
                l -= 1
            cur -= 1

        while r >= 0:
            nums1[cur] = nums2[r]
            r -= 1
            cur -= 1
