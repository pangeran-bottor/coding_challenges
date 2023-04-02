import bisect
import math
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        n, m = len(spells), len(potions)
        pairs = []
        potions.sort()

        for spell in spells:
            target = math.ceil(success / spell)
            idx = bisect.bisect_left(potions, target)
            pairs.append(m - idx)
        return pairs
