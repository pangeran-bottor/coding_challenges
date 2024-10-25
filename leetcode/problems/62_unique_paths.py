class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        f(x, y) : number of possible unique paths at x, y

                with only RIGHT or DOWN

        f(0, 0) = 1

        f(0, 1) = [f(0, 0) + RIGHT] = 1
        f(1, 0) = [f(0, 0) + DOWN] = 1
        f(1, 1) = [f(0, 1) + f(1, 0)] = 2

        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = 1

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if (row, col) == (1, 1):
                    continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m][n]
