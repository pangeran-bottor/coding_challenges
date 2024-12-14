from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = set()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    curr = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr == target:
                        ans.add(tuple((nums[i], nums[j], nums[left], nums[right])))
                        left += 1
                    elif curr < target:
                        left += 1
                    else:
                        right -= 1
        return list(ans)
