from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remains = []
        ans = 0
        for c, r in zip(capacity, rocks):
            if r < c:
                remains.append(c-r)
            else:
                ans += 1
        
        remains.sort()
        for r in remains:
            if additionalRocks < r:
                break
            ans += 1
            additionalRocks -= r

        return ans
