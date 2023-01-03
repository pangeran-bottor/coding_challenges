from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        r, c = len(strs), len(strs[0])

        for i in range(c):
            for j in range(r - 1):
                if strs[j][i] > strs[j + 1][i]:
                    count += 1
                    break

        return count
