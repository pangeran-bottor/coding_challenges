from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def dp(last_idx, remains):
            if remains == 1:
                return max(jobDifficulty[last_idx:])

            curr = float("inf")
            max_diff = 0
            for i in range(last_idx, n - remains + 1):
                max_diff = max(max_diff, jobDifficulty[i])
                curr = min(curr, max_diff + dp(i + 1, remains - 1))

            return curr

        n = len(jobDifficulty)
        if n < d:
            return -1
        return dp(0, d)
