from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        ans = []
        for interval in intervals:
            if len(ans) == 0:
                ans.append(interval)
            elif ans[-1][-1] >= interval[0]:
                ans[-1][-1] = max(ans[-1][-1], interval[1])
            else:
                ans.append(interval)
        return ans
