from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def is_valid(word, allowed_set):
            for ch in word:
                if ch not in allowed_set:
                    return False
            return True
        allowed_set = set(allowed)
        ans = 0
        for word in words:
            if is_valid(word, allowed_set):
                ans += 1
        return ans
