from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        N = len(intervals)
        for i in range(N-1):
            if intervals[i][1] <= intervals[i+1][0]:
                continue
            
            ans += 1
            intervals[i+1] = intervals[i]
        return ans
