from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        c = []
        freq = [0 for _ in range(n + 1)]

        curr_count = 0
        for a, b in zip(A, B):
            freq[a] += 1
            if freq[a] == 2:
                curr_count += 1

            freq[b] += 1
            if freq[b] == 2:
                curr_count += 1

            c.append(curr_count)
        return c
