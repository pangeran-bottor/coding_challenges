import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(h)

        for stone in stones:
            heapq.heappush(h, -1 * stone)

        while len(h) > 1:
            max1 = -heapq.heappop(h)
            max2 = -heapq.heappop(h)

            if max1 != max2:
                heapq.heappush(h, -1 * abs(max1 - max2))

        return -heapq.heappop(h) if h else 0
