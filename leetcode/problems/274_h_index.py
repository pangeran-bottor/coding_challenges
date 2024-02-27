from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0] * 1001
        for cite in citations:
            counts[cite] += 1

        h = 0
        for i in range(1000, -1, -1):
            h += counts[i]
            if i <= h:
                return i
