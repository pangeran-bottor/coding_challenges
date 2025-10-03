class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            count = 0
            while 0 <= left and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        counts = 0
        n = len(s)

        for i in range(n):
            counts += expand(i, i)
            counts += expand(i, i + 1)
        return counts
