class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        N = len(s)
        dp = [0] * (N + 1)

        dp[0] = 1
        dp[1] = 1
        for i in range(1, N):
            one_char = int(s[i:i + 1])
            two_chars = int(s[i-1:i + 1])

            if 1 <= one_char <= 9:
                dp[i+1] += dp[i]
            if 10 <= two_chars <= 26:
                dp[i+1] += dp[i-1]
        return dp[N]
