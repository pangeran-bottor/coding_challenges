from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)

        common = 0
        for ch, ct in s_counter.items():
            common += min(ct, t_counter.get(ch, 0))

        ans = len(s) - common
        return ans
