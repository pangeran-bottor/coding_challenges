class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        ones = 0
        for ch in s:
            if ch == "0":
                # let dp[i] is the answer for s[0..i].
                # then to solve dp[n], either:
                # - dp[n-1] + 1, by changing this last "0" into "1"
                # - or, change all "1" found so far
                ans = min(ans + 1, ones)
            else:
                ones += 1
        return ans
