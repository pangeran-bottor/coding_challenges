# https://leetcode.com/contest/weekly-contest-308/problems/longest-subsequence-with-limited-sum/

import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        for i in range(1, N):
            nums[i] += nums[i-1]
        
        answer = []
        for q in queries:
            if q >= nums[-1]:
                answer.append(N)
            else:
                idx = bisect.bisect_left(nums, q)
                if nums[idx] == q:
                    idx += 1
                answer.append(idx)
        return answer
