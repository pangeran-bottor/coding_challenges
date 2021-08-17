from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # since one of the constraint is 1 <= accounts[i][j] <= 100
        ans = 0
        for account in accounts:
            ans = max(ans, sum(account))
        return ans
