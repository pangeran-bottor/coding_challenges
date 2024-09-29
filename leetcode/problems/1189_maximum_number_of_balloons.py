from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        balloon:
            b -> 1
            a -> 1
            n -> 1
            l -> 2
            o -> 2

        b,a,n -> ban_min = min(bCount, aCount, nCount)
        l, o  -> lo_min = min(lCount, oCount) // 2

        ans = min(ban_min, lo_min)
        """
        counts = Counter(text)
        ban_min = min(counts["b"], counts["a"], counts["n"])
        lo_min = min(counts["l"], counts["o"]) // 2
        return min(ban_min, lo_min)
