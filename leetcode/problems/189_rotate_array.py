from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_in_place(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n = len(nums)
        k %= n

        reverse_in_place(nums, 0, n - k - 1)
        reverse_in_place(nums, n - k, n - 1)
        nums.reverse()
