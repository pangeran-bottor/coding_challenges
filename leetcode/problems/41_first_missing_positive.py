from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # O(N) time, O(N) space
        # TODO: O(1) space
        N = len(nums)
        tmp = [0 for i in range(N)]
        for num in nums:
            if 0 < num <= N:
                tmp[num-1] += 1
        
        for idx, val in enumerate(tmp):
            if val == 0:
                return idx + 1
        return N + 1
