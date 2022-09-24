from heapq import heappop, heappush
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_heap = []
        ans = 0
        
        intervals.sort()
        for interval in intervals:
            if len(min_heap) == 0 or min_heap[0] > interval[0]:
                heappush(min_heap, interval[1])
                ans += 1
            else:
                heappop(min_heap)
                heappush(min_heap, interval[1])
        return ans
