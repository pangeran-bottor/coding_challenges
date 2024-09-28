class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, n1 = 0, len(s)
        p2, n2 = 0, len(t)

        while p1 < n1 and p2 < n2:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return p1 == n1
