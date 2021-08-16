from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        # naive solution
        #
        # ans = []
        # for i in range(len(nums)):
        #     el = nums[nums[i]]
        #     ans.append(el)
        # return ans

        # O(1) space
        #
        N = len(nums)
        for i in range(N):
            nums[i] += (N * (nums[nums[i]] % N))
        for i in range(N):
            nums[i] //= N
        return nums
