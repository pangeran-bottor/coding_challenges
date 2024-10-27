from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # from functools import cache

        # @cache
        # def dp(row, col):
        #     if not ((0 <= row < len(matrix)) and (0 <= col < len(matrix[0]))):
        #         return 0

        #     if matrix[row][col] == "0":
        #         return 0

        #     return 1 + min(dp(row-1,col-1), dp(row-1, col), dp(row, col-1))

        # ans = 0
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == "0":
        #             continue
        #         count = dp(row, col)
        #         ans = max(ans, count)
        # return ans**2

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        ans = 0
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if matrix[row - 1][col - 1] != "1":
                    continue

                dp[row][col] = (
                    min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
                )
                ans = max(ans, dp[row][col])

        return ans**2
