from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        is_removed = False
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                if is_removed:
                    return False

                # If nums[i-2] >= nums[i], it means nums[i] cannot be part of the sequence
                # as it violates the strictly increasing property.
                # To "remove" nums[i], we assign nums[i] = nums[i-1]. This adjustment ensures
                # the sequence remains valid without explicitly deleting an element.
                #
                # else, if nums[i-2] < nums[i] <= nums[i-1], we move the nums[i]
                # to nums[i -1], practically "removing" nums[i-1]
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
                is_removed = True
        return True
