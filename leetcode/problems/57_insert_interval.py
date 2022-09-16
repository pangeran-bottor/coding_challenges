from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        # TODO: implement optimized solution
        
        intervals.append(newInterval)
        intervals.sort()
        
        for interval in intervals:
            if len(ans) == 0:
                ans.append(interval)
            elif ans[-1][-1] >= interval[0]:
                ans[-1][-1] = max(ans[-1][-1], interval[1])
            else:
                ans.append(interval)
        return ans
