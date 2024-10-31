from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(curr_idx):
            if curr_idx < 0:
                return True

            for word in wordDict:
                if (curr_idx >= len(word) - 1) and dp(curr_idx - len(word)):
                    if s[curr_idx - len(word) + 1 : curr_idx + 1] == word:
                        return True
            return False

        return dp(len(s) - 1)
