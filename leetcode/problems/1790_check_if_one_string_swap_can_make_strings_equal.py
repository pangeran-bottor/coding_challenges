class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                diffs.append([ch1, ch2])
        if len(diffs) not in (0, 2):
            return False

        if len(diffs) == 2 and (
            diffs[0][0] != diffs[1][1] or diffs[0][1] != diffs[1][0]
        ):
            return False

        return True
