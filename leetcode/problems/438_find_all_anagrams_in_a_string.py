import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        target = collections.Counter()
        for ch in p:
            target[ch] += 1

        curr = collections.Counter()
        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return ans
        for i in range(len_p):
            curr[s[i]] += 1

        start_idx = 0
        while start_idx <= len_s - len_p:
            if curr == target:
                ans.append(start_idx)

            start_idx += 1

            if start_idx <= len_s - len_p:
                curr[s[start_idx - 1]] -= 1
                curr[s[start_idx + len_p - 1]] += 1

        return ans
