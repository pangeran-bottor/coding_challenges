import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-1 * pile for pile in piles]
        heapq.heapify(piles)

        while k > 0:
            cur_max = -1 * heapq.heappop(piles)
            heapq.heappush(piles, -1 * (cur_max - cur_max // 2))
            k -= 1

        print(piles)
        return sum([-1 * pile for pile in piles])
